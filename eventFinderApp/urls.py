from django.urls import path
from . import views

app_name = 'eventFinderApp'

urlpatterns = [
    # event-finder/
    path('', views.IndexView.as_view(), name='index'),
    # event-finder/1
    path('<int:pk>/', views.EventView.as_view(), name='event'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    # add event-finder/newEvent
    path('createEvent/', views.CreateEventView.as_view(), name='CreateEvent'),
]
