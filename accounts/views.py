from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,UserChangeForm, PasswordChangeForm
from accounts.form import RegistrationForm, EditProfileForm
from accounts.serailizer import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth import login

# Create your views here.


def register(request):
    if request.method == 'POST':
        serialize = UserSerializer(data=request.POST)
        if serialize.is_valid():
            user = serialize.save()            
            login(request, user)
            return redirect('/accounts/profile')
        else:
            form = RegistrationForm()
            args = {'form':form}
            return render(request, 'accounts/reg_form.html',args)
    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request, 'accounts/reg_form.html',args)

@login_required(login_url='/accounts/login')
def view_profile(request):
    args = {'user':request.user}
    return render(request, 'accounts/profile.html',args)


@login_required(login_url='/accounts/login')
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
        
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form':form}
        return render(request, 'accounts/edit_profile.html',args)


@login_required(login_url='/accounts/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/accounts/profile/')
        else:
            return redirect('/accounts/profile/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request, 'accounts/change_password.html',args)      