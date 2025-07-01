from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_student, name='add_student'),
    path('view/', views.view_students, name='view_students'),
    path('search/', views.search_student, name='search_student'),
    path('delete/<int:roll_number>/', views.delete_student, name='delete_student'),
    path('exit/', views.exit_confirm, name='exit_confirm'),
    path('', views.student_home, name='student_home'),#
]