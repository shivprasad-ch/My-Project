from django.contrib import admin
from django.urls import path, include

from django.contrib import admin
from django.urls import path, include
from student import views  # ✅ हे import जोडा

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.student_home, name='student_home'),
    path('students/', include('student.urls')),
]