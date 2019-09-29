from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from . import views

app_name = 'users'

urlpatterns = [


    path('register/', views.Register.as_view(), name='register'),

    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^profile/edit_profile/$',
        views.EditProfile.as_view(), name='editprofile'),

    # url(r'^logout/$', views.logout_request, name='logout'),
    # url(r'^login/$', views.login_view, name="login"),

    url(r'^password_change/$', views.PasswordChangeView.as_view(),
        name='password_change'),

    url(r'^password_change/done/$', views.PasswordChangeDoneView.as_view(),
        name='password_change_done'),

    url(r'^password_reset/$', views.PasswordResetView.as_view(), name='password_reset'),

    url(r'^password_reset/done/$', views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),

    url(r'^reset/<uidb64>/<token>/$',
        views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),


    # path('<int:pk>/', views.ProfileView.as_view(), name="profile")

]
