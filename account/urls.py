from django.urls import path
from . import views
from django.contrib.auth.views import login, logout

#defines all 'account' urls so when the user visits /account/SOMETHING
urlpatterns = [
    path('', views.account),
    path('login/', login, {'template_name': 'account/login.html'}),
    path('logout/', logout, {'template_name': 'account/logout.html'}),
    path('register/', views.register, name='register'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit', views.edit_profile, name='edit_profile')
]