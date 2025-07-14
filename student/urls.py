from django.urls import path
from . import views
from .views import StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView

urlpatterns = [
    # 🌐 UI-based views
    path('add/', views.add_student, name='add_student'),
    path('view/', views.view_students, name='view_students'),
    path('search/', views.search_student, name='search_student'),
    path('delete/<int:roll_number>/', views.delete_student, name='delete_student'),
    path('exit/', views.exit_confirm, name='exit_confirm'),
    path('', views.student_home, name='student_home'),

    # 🔗 API endpoints (DRF)
    path('api/students/', StudentListCreateAPIView.as_view(), name='api_student_list_create'),
    path('api/students/<int:roll_number>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='api_student_detail'),
]