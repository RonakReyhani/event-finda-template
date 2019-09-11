
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Event, User
from .forms import createEvent ,Account
from django.core.files.storage import FileSystemStorage
from bootstrap_modal_forms.generic import BSModalLoginView


class UserCreateView(BSModalLoginView):
    authentication_form = Account
    template_name = 'eventFinderApp/account.html'
    success_message = 'Success: You were successfully logged in.'
    extra_context = dict(success_url=reverse_lazy('eventFinderApp:index'))

class IndexView(generic.ListView):
    template_name = 'eventFinderApp/index.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        '''Return the events.'''
        return Event.objects.all()


class EventView(generic.DetailView):
    model = Event
    template_name = 'eventFinderApp/event.html'

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
        if createEvent.is_valid():
            createEvent.save()
            # redirect to the list of events 
            return HttpResponseRedirect(self.success_url)
        # if the form isn't valid return the form (with automatic errors)
        # build the response with our template
        return render(request, self.template, self.form_context(createEvent))  











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