from django.shortcuts import render

# Create your views here.

#when the user goes to /account/, render index.html in the accounts folder in the templates folder
def account(request):
    return render(request, "account/index.html")