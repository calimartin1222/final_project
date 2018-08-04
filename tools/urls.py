from django.urls import path
from . import views
from django.contrib.auth.views import login

#defines all 'tools' urls so when the user visits /SOMETHING
urlpatterns = [
    path('', views.home),
]