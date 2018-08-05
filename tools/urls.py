from django.urls import path
from . import views

#defines all 'tools' urls so when the user visits /SOMETHING
urlpatterns = [
    path('', views.home),
    path('per_day/', views.per_day, name='per_day'),
    path('grade_recieved/', views.grade_recieved, name='grade_recieved'),
]