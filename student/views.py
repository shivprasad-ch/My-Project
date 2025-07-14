from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm

# 1. Add student
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_students')
    else:
        form = StudentForm()
    return render(request, 'student/add_student.html', {'form': form})

# 2. View all students
def view_students(request):
    students = Student.objects.all()
    return render(request, 'student/view_students.html', {'students': students})

# 3. Search student by roll number (HTML Form)
def search_student(request):
    student = None
    error = None
    if request.method == 'POST':
        roll = request.POST.get('roll_number')
        try:
            student = Student.objects.get(roll_number=roll)
        except Student.DoesNotExist:
            error = "Student not found."
    return render(request, 'student/search_student.html', {'student': student, 'error': error})

# 4. Delete student (with confirmation)
def delete_student(request, roll_number):
    student = get_object_or_404(Student, roll_number=roll_number)
    if request.method == 'POST':
        student.delete()
        return redirect('view_students')
    return render(request, 'student/confirm_delete.html', {'student': student})

# 5. Exit confirmation
def exit_confirm(request):
    if request.method == 'POST':
        confirm = request.POST.get('confirm')
        if confirm == 'yes':
            return render(request, 'student/goodbye.html')
        else:
            return redirect('view_students')
    return render(request, 'student/exit_confirm.html')

# 6. Home page
def student_home(request):
    return render(request, 'student/home.html')

# ------------------------------------------------------
# ✅ API Views (Django REST Framework - with exact search)
# ------------------------------------------------------
from rest_framework import generics
from .serializers import StudentSerializer

# ✅ List + Create API: /api/students/?search=1
class StudentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all()
        search_value = self.request.GET.get('search', None)

        if search_value is not None:
            if search_value.isdigit():  # exact match for roll number
                queryset = queryset.filter(roll_number=int(search_value))
            else:  # partial match for name
                queryset = queryset.filter(name__icontains=search_value)

        return queryset

# ✅ Retrieve + Update + Delete API: /api/students/<roll_number>/
class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'roll_number'