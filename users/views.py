from django.contrib.auth import update_session_auth_hash
from users.forms import CustomUserCreationForm, CustomUserChangeForm
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import CustomUser
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


class Register(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


class ProfileView(generic.View):
    template_name = "registration/profile.html"
    context_object_name = 'events_list'

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.filter(host=self.request.user).order_by('start_time')


class EditProfile(generic.UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('eventFinderApp:account')
    template_name = 'registration/editprofile.html'

    def get_object(self, queryset=None):
        return self.request.user


def logout_request(request):
    logout(request)
    messages.info(request, " Logged out successfully!")
    return HttpResponseRedirect(reverse_lazy("eventFinderApp:index"))


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
