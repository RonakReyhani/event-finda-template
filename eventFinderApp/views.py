
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic import CreateView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Event
from users.models import CustomUser
from .forms import createEvent
from django.core.files.storage import FileSystemStorage
from bootstrap_modal_forms.generic import BSModalLoginView
from django.views.generic.edit import UpdateView
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.db.models import Count
from django.contrib.auth.decorators import login_required

from django.views.generic.base import TemplateView
# class ProfileView(generic.DetailView):
#     model = CustomUser
#     template_name = "profile.html"
#     context_object_name = 'profile_view'

#     def get_queryset(self):
#         '''Return the events.'''
#         return Event.objects.filter(created_by=self.request.user).order_by('start_time')


class ProfileView(generic.ListView):
    template_name = 'eventFinderApp/profile.html'
    context_object_name = 'events_list'

    def get_object(self, queryset=None):
        return self.request.user

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.filter(created_by=self.request.user).order_by('start_time')


# class EditProfile(generic.UpdateView):
#     form_class = CustomUserChangeForm
#     success_url = reverse_lazy('eventFinderApp:profile')
#     template_name = 'registration/editprofile.html'


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = CustomUser
    fields = ('first_name', 'last_name', 'email', 'image')
    template_name = 'eventFinderApp/edit_profile.html'
    success_url = reverse_lazy('eventFinderApp:profile')

    def get_object(self):
        return self.request.user


class IndexView(generic.ListView):
    model = Event
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'
    paginate_by = 6

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     list_films = Film.objects.all()
    #     paginator = Paginator(list_films, self.paginate_by)

    #     page = self.request.GET.get('page')
    # def get_context_data(self, **kwargs):
    #     kwargs['event'] = self.Event
    #     return super().get_context_data(**kwargs)

    # def get_queryset(self):
    #     self.event = get_object_or_404(
    #         Event, pk=self.kwargs.get('pk'))
    #     queryset = self.event.objects.all().order_by(
    #         'start_time').annotate(replies=Count('event') - 1)
    #     return queryset

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.all().order_by(
            'start_time')


class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'


# def Profile(request):
#     accountform = ProfileForm()
#     return render(request, 'eventFinderApp/profile.html', {'accountform': accountform})


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


@method_decorator(login_required, name='dispatch')
class EditEventView(generic.UpdateView):
    model = Event
    form_class = createEvent
    success_url = reverse_lazy('eventFinderApp:profile')
    template_name = 'eventFinderApp/editEvent.html'


@login_required
def event_remove(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.user == event.created_by:
        Event.objects.filter(id=event_id).delete()
        return redirect('eventFinderApp:profile')


# @login_required
# def event_edit(request, post_id):
#     event = Event.objects.get(pk=event_id)
#     if request.user == event.created_by:
#         if request.method == 'POST':
#             form = createEvent(request.POST, instance=event)
#             if form.is_valid():
#                 form.save()
#                 return redirect('eventFinderApp:profile')

#         else:
#             form = createEvent(instance=event)

#     args = {}
#     args.update(csrf(request))
#     args['form'] = form

#     return render_to_response('eventFinderApp/event_update_form.html', args)
