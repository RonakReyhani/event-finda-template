
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


class ProfileView(TemplateView):
    template_name = 'eventFinderApp/profile.html'


# class EditProfile(generic.UpdateView):
#     form_class = CustomUserChangeForm
#     success_url = reverse_lazy('eventFinderApp:profile')
#     template_name = 'registration/editprofile.html'

#     def get_object(self, queryset=None):
#         return self.request.user


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    model = CustomUser
    fields = ('first_name', 'last_name', 'email', 'image')
    template_name = 'eventFinderApp/edit_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user


class IndexView(generic.ListView):
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        kwargs['event'] = self.Event
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.event = get_object_or_404(
            Event, pk=self.kwargs.get('pk'))
        queryset = self.Event.order_by(
            'start_time').annotate(replies=Count('event') - 1)
        return queryset

    # def get_queryset(self):
    #     '''Return the events.'''
    #     return Event.objects.all()


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
class UpdateEventView(UpdateView):
    model = Event
    fields = '__all__'
    template_name = 'event_update_form.html'
    pk_url_kwarg = 'event_pk'
    context_object_name = 'event'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)

    def form_valid(self, form):
        event = form.save(commit=False)
        event.updated_by = self.request.user
        event.updated_at = timezone.now()
        event.save()
        return redirect('users:profile', pk=post.topic.board.pk, topic_pk=post.topic.pk)


# def CreateEventView(request):
#         if request.method == 'POST':
#             # POST, generate form with data from the request
#             form = createEvent(request.POST)
#             # check if it's valid:
#             if form.is_valid():
#                 # process data, insert into DB, generate email,etc
#                 # redirect to a new url:
#                 form.save()
#                 return HttpResponseRedirect('eventFinderApp/index.html')
#         else:
#             # GET, generate blank form
#             form = createEvent()
#         return render(request,'eventFinderApp/createEvent.html',{'form':form})
#
#

# class AddEventCreateView(generic.CreateView):
#     # using the create view we can just give it the variables
#     # as the functionaity is already built in!
#     form_class = EventForm
#     template_name = 'eventFinderApp/addevent.html'
#     success_url = reverse_lazy('eventFinderApp:index')
#     # we have to use reverse_lazy so that urls.py can load our class
#     # and not get stuck in a recursive loop
