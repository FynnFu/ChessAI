from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit-profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
