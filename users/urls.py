from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from . import views

app_name = 'users'

urlpatterns = [


    path('register/', views.Register.as_view(), name='register'),
    # path('<int:pk>/', views.EditProfile.as_view(), name='editprofile'),
    # url(r'^editProfile/<int:pk>$', views.EditProfile.as_view(), name='editprofile'),
    url(r'^logout/$', views.logout_request, name='logout'),
    # url(r'^login/$', views.login_view, name="login"),
    path(
        'password_change/',
        auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
    path(
        'password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),

    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html', email_template_name='registration/password_reset_email.html', subject_template_name='registration/password_reset_subject.txt'), name='password_reset'),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    # url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    # url(r'^password_reset/done/$', auth_views.password_reset_done,
    #     name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     auth_views.password_reset_confirm, name='password_reset_confirm'),
    # url(r'^reset/done/$', auth_views.password_reset_complete,
    #     name='password_reset_complete'),
]
