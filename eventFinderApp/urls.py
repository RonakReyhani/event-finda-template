from django.urls import path
from . import views

app_name = 'eventFinderApp'

urlpatterns = [
    # event-finder/
    path('', views.IndexView.as_view(), name='index'),
    # event-finder/1
    path('<int:pk>/', views.EventView.as_view(), name='event'),
    # event-finder/my-account
    path('account/', views.UserCreateView.as_view(), name='account'),
    #add event-finder/newEvent
    path('createEvent/', views.CreateEventView.as_view(), name='CreateEvent'),
]