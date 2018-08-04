from django.shortcuts import render, redirect
from account.forms import registration_form, edit_profile_form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

# Create your views here.

#when the user goes to /account/, render index.html in the accounts folder in the templates folder
def account(request):
    return render(request, "account/index.html")

def register(request):

    if request.method == "POST":
        form = registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/login/')
    else:
        form = registration_form()
        args = {
            'form': form
        }
        return render(request, 'account/register.html', args)

def view_profile(request):

    args = {
        'user' : request.user
    }

    return render(request, 'account/profile.html', args)

def edit_profile(request):

    if request.method == "POST":
        form = edit_profile_form(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile/')
    else:
        form = edit_profile_form(instance=request.user)
        args = {
            'form': form
        }
        return render(request, 'account/edit.html', args)