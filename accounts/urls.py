from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views
from accounts.api import views as api_view

app_name = 'accounts'

urlpatterns = [
    path('login', LoginView.as_view(template_name='accounts/login.html')),
    path('profile/logout', LogoutView.as_view(template_name='accounts/logout.html')),
    path('register', api_view.registration_view, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('profile/change-password', views.change_password, name='chnage_password'),
]
