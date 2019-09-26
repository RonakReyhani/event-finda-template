from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import RegisterForm, UsersLoginForm
from .models import customUser, Profile
from django import forms
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.views import generic
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.db import transaction
from eventFinderApp.models import Event
from django.contrib.auth.views import PasswordContextMixin
from django.views.generic.edit import FormView
from django.views.generic import TemplateView


def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'registration/register.html'
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():

            if customUser.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password1'] != form.cleaned_data['password2']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = customUser.objects.create_user(

                    form.cleaned_data['email'],
                    form.cleaned_data['password1']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()

                # Login the user
                login(request, user)

                # redirect to accounts page:
                return HttpResponseRedirect(reverse_lazy('eventFinderApp:index'))

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, " Logged out successfully!")
    return HttpResponseRedirect(reverse_lazy("eventFinderApp:index"))


@csrf_protect
def login_view(request):
    if request.method == 'POST':
        form = UsersLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.info(
                    request, f'You are now logged in as {{user.first_name}}')
                return HttpResponseRedirect(reverse_lazy("eventFinderApp:index"))
            else:
                messages.error(request, "Invalid email or password")
        else:
            messages.error(request, "Invalid email or password")
    form = UsersLoginForm()
    return render(request, "registration/login.html", {'form': form})


class PasswordResetView(PasswordContextMixin, FormView):
    template_name = 'registration/password_reset_form.html'


class PasswordResetDoneView(PasswordContextMixin, TemplateView):
    template_name = 'registration/password_reset_done.html'


class PasswordResetConfirmView(PasswordContextMixin, FormView):
    template_name = 'registration/password_reset_confirm.html'


class PasswordChangeView(PasswordContextMixin, FormView):
    template_name = 'registration/password_change_form.html'


class PasswordChangeDoneView(PasswordContextMixin, TemplateView):
    template_name = 'registration/password_change_done.html'


class ProfileView(generic.DetailView):
    model = Profile
    template_name = 'registration/profile.html'

    def get_queryset(self):
        '''Return the events created_by user'''
        return Event.objects.filter(created_by=self.request.user)


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _(
                'Your profile was successfully updated!'))
            return redirect('users:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = RegisterForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'registration/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
