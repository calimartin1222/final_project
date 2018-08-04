from django.shortcuts import render
from tools.forms import per_day_form

# Create your views here.
def home(request):
    return render(request, 'tools/home.html')

def per_day(request):
    #checks the way the user got to the page
    #if it was a POST method, execute the following code
    if request.method == "POST":
        #creates a new form object that is based off of a custom form called
        #per_day_form from forms.py
        form = per_day_form(request.POST, instance=request.user)
        #checks if there's anything wrong with the user input (ex. SQL inserts)
        if form.is_valid():
            #saves the form with the entered information
            form.save()
            #redirects the user to the same page and shows results
            return redirect('/per_day/', )
    else:
        #creates a new, blank per_day_form for the user ot fill out
        form = per_day_form(instance=request.user)
        #creates a dictionary to be passed with the form information
        args = {
            'form': form
        }
        #renders per_day.html in the accounts folder in the templates
        #folder, and passes the dictionary args as an argument
        return render(request, 'account/per_day.html', args)