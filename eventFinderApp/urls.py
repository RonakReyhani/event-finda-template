from django.urls import path
from . import views
from django.conf.urls import url


app_name = 'eventFinderApp'

urlpatterns = [
    # event-finder/
    path('', views.IndexView.as_view(), name='index'),
    # event-finder/1 view event
    path('<int:pk>/', views.EventView.as_view(), name='event'),
    # add event-finder/newEvent
    path('createEvent/', views.CreateEventView.as_view(), name='CreateEvent'),

    path('edit/<int:pk>/', views.EditEventView.as_view(), name='update-event'),
    # url(r'^(?P<event_pk>\d+)/edit/$',
    #         views.UpdateEventView.as_view(), name='update-event'),

    # edit and remove event
    url(r'^remove/(?P<event_id>\d+)/$', views.event_remove, name='remove-event'),
    #     url(r'^edit/(?P<event_id>\d+)/$', views.event_edit, name='update-event'),

    # view profile
    path('profile/',
         views.ProfileView.as_view(), name='profile'),
    # update profile
    path('profile/<int:pk>/edit/',
         views.ProfileUpdateView.as_view(), name='editprofile'),


]
