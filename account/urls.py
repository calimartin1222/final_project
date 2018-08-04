from django.urls import path
from . import views
from django.contrib.auth.views import login

#defines all 'account' urls so when the user visits /account/SOMETHING
urlpatterns = [
    path('', views.account),
    path('login/', login, {'template_name': 'account/login.html'})
]