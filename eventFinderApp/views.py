
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic import CreateView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Event, Account
from users.models import CustomUser
from .forms import createEvent, AccountForm
from django.core.files.storage import FileSystemStorage
from bootstrap_modal_forms.generic import BSModalLoginView
from django.views.generic.edit import UpdateView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from users.forms import CustomUserChangeForm


# class ProfileView(generic.ListView):
#     template_name = 'eventFinderApp/profile.html'
#     context_object_name = 'events_list'

#     def get_object(self, queryset=None):
#         return self.request.user

#     def get_queryset(self):
#         '''Return the events.'''
#         return Event.objects.filter(created_by=self.request.user).order_by('start_time')

class IndexView(generic.ListView):
    model = Event
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'
    paginate_by = 6

    def get_queryset(self):
        now = timezone.now()
        return Event.objects.filter(start_time__gte=now).order_by('start_time')


class AccountView(generic.DetailView):
    model = Account
    template_name = 'eventFinderApp/account.html'
    context_object_name = 'events_list'

    def get_object(self, queryset=None):
        return self.request.user

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.filter(created_by=self.request.user).order_by('start_time')


# def account(request):
#     accountform = AccountForm()
#     return render(request, 'eventFinderApp/account.html', {'accountform': accountform})

def account(request):
    events_list = Event.objects.filter(created_by=request.user)
    if request.method == 'POST':
        print(request.POST)
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = CustomUserChangeForm(instance=request.user)
    context = {'events_list': events_list, 'form': user_form}
    template_name = 'eventFinderApp/account.html'
    return render(request, template_name, context)


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = CustomUser
    fields = ('first_name', 'last_name', 'email', 'image')
    template_name = 'eventFinderApp/edit_profile.html'
    success_url = reverse_lazy('eventFinderApp:account')

    def get_object(self):
        return self.request.user


class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'


def add_event(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            event = form.save(commit=False)
            event.host = request.user
            event.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')

            return HttpResponseRedirect(reverse('eventFinderApp:index'))
        return render(request, 'eventFinderApp/newEventForm.html', {'eventform': form})
    # if a GET (or any other method) we'll create a blank form
    else:
        eventform = EventForm()
        return render(request, 'eventFinderApp/newEventForm.html', {'eventform': eventform})


class CreateEventView(generic.View):
        # shared variables can now go here
    template = 'eventFinderApp/createEvent.html'
    form_class = createEvent
    success_url = reverse_lazy('eventFinderApp:index')
    # we can create the context in one place too

    def form_context(self, createEvent):
        # assign the form to the context
        return {'createEvent': createEvent}
    # in the class basded view we handle the GET request with a get() function

    def get(self, request):
        # create our form instance
        createEvent = self.form_class()
        # return our template with our contex
        return render(request, self.template, self.form_context(createEvent))
    # in the class based view we handle the POST request with a post() function

    def post(self, request):
        # we create our form instance with the data from the request
        createEvent = self.form_class(request.POST, request.FILES)
        file = request.FILES['event_image']
        # check if the form is valid
        if not request.user.is_authenticated:
            raise Http404
        if createEvent.is_valid():
            instance = createEvent.save(commit=False)
            instance.created_by = request.user
            instance.save()

            # redirect to the list of events
            return HttpResponseRedirect(self.success_url)
        # if the form isn't valid return the form (with automatic errors)
        # build the response with our template
        return render(request, self.template, self.form_context(createEvent))


class EditEvent(generic.UpdateView):
    model = Event
    form_class = createEvent
    template_name = 'eventFinderApp/createEvent.html'
    success_url = reverse_lazy('eventFinderApp:index')
    context_object_name = 'name'

    def get_queryset(self):
        # only allow logged in user to edit their own events
        return self.model.objects.filter(host=self.request.user)
