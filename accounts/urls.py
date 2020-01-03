from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='index'),
    path('login', LoginView.as_view(template_name='accounts/login.html')),
]
