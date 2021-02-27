from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import CustomUserCreationForm


def register(request):
    if request.method != 'POST':
        form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('e_shop:home')
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password was successfully changed")
            return redirect('users:change_password')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})

