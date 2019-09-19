from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.conf.urls import url

from . import views

app_name = 'users'

urlpatterns = [
    url(r'^register/$', views.user_register, name='user_register'),
    url(r'^logout/$', views.logout_request, name='logout'),
    url(r'^login/$', views.login_request, name='login'),


]
