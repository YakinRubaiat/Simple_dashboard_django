from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='index'),
    path('login', LoginView.as_view(template_name='accounts/login.html')),
    path('logout', LogoutView.as_view(template_name='accounts/logout.html')),
    path('register', views.register, name='register'),
    path('profile', views.view_profile, name='view_profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
]
