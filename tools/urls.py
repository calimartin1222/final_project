from django.urls import path
from . import views

#defines all 'tools' urls so when the user visits /SOMETHING
urlpatterns = [
    path('', views.home),
    path('per_day/', views.per_day, name='per_day'),
    path('grade_recieved/', views.grade_recieved, name='grade_recieved'),
    path('semester_grade/', views.semester_grade, name='semester_grade'),
    path('tasklist/', views.tasklist, name='tasklist'),
    path('timer/', views.timer, name='timer'),
]