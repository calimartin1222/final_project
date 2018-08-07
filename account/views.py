from django.shortcuts import render, redirect
from account.forms import registration_form, edit_profile_form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required

@login_required
def account(request):
    user = request.user
    #renders index.html in the accounts folder in the templates folder
    args = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
    }
    return render(request, "account/index.html", args)

def register(request):
    #checks the way the user got to the page
    #if it was a POST method, execute the following code
    if request.method == "POST":
        #creates a new form object that is based off of a custom form called
        #registration_form from forms.py
        form = registration_form(request.POST)
        #checks if there's anything wrong with the user input (ex. SQL inserts)
        if form.is_valid():
            #saves the form with the entered information
            form.save()
            #redirects the user to login page
            return redirect('/account/login/')
    #if the request was not a POST method (GET), execute the following code
    else:
        #creates a new, blank registration form for the user to fill out
        form = registration_form()
        #creates a dictionary to be passed with the form information
        args = {
            'form': form
        }
        #renders register.html in the accounts folder in the templates
        #folder, and passes the dictionary args as an argument
        return render(request, 'account/register.html', args)

@login_required
def edit_profile(request):
    #checks the way the user got to the page
    #if it was a POST method, execute the following code
    if request.method == "POST":
        #creates a new form object that is based off of a custom form called
        #edit_profile_form from forms.py
        form = edit_profile_form(request.POST, instance=request.user)
        #checks if there's anything wrong with the user input (ex. SQL inserts)
        if form.is_valid():
            #saves the form with the entered information
            form.save()
            #redirects the user to their profile page to see the changes
            #they made and double check
            return redirect('/account/')
    else:
        #creates a new, blank edit profile form for the user ot fill out
        form = edit_profile_form(instance=request.user)
        #creates a dictionary to be passed with the form information
        args = {
            'form': form
        }
        #renders edit.html in the accounts folder in the templates
        #folder, and passes the dictionary args as an argument
        return render(request, 'account/edit.html', args)