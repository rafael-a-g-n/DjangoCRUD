from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Instructor
from django import forms

# Form for Course
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']

# Form for Instructor
class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['name', 'description']

# List all courses
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'crud/course_list.html', {'courses': courses})

# Create a new course
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'crud/course_form.html', {'form': form})

# Update an existing course
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'crud/course_form.html', {'form': form})

# Delete a course
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'crud/course_confirm_delete.html', {'course': course})

# List all instructors
def instructor_list(request):
    instructors = Instructor.objects.all()
    return render(request, 'crud/instructor_list.html', {'instructors': instructors})

# Create a new instructor
def instructor_create(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:instructor_list')
    else:
        form = InstructorForm()
    return render(request, 'crud/instructor_form.html', {'form': form})

# Update an existing instructor
def instructor_update(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    if request.method == 'POST':
        form = InstructorForm(request.POST, instance=instructor)
        if form.is_valid():
            form.save()
            return redirect('crud:instructor_list')
    else:
        form = InstructorForm(instance=instructor)
    return render(request, 'crud/instructor_form.html', {'form': form})

# Delete an instructor
def instructor_delete(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    if request.method == 'POST':
        instructor.delete()
        return redirect('crud:instructor_list')
    return render(request, 'crud/instructor_confirm_delete.html', {'instructor': instructor})
