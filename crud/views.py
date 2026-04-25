# Enrollment update view
def enrollment_update(request, pk):
    """Update an existing enrollment."""
    from crud.models import Enrollment
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('crud:course_detail', pk=enrollment.course.pk)
    else:
        form = EnrollmentForm(instance=enrollment)
    return render(request, 'crud/enrollment_form.html', {'form': form, 'course': enrollment.course})
"""Views for CRUD app models."""

from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from crud.models import Course, Instructor, Learner
from crud.forms import InstructorForm, LearnerForm, EnrollmentForm, CourseForm
# Enrollment create view
def enrollment_create(request, course_id):
    """Create a new enrollment for a learner in a course."""
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.course = course
            enrollment.save()
            return redirect('crud:course_detail', pk=course_id)
    else:
        form = EnrollmentForm(initial={'course': course})
    return render(request, 'crud/enrollment_form.html', {'form': form, 'course': course})




def course_list(request):
    """List all courses."""
    courses = Course.objects.all()
    return render(request, 'crud/course_list.html', {'courses': courses})


def course_create(request):
    """Create a new course."""
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:course_list')
    else:
        form = CourseForm()
    return render(request, 'crud/course_form.html', {'form': form})


def course_update(request, pk):
    """Update an existing course."""
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('crud:course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'crud/course_form.html', {'form': form})


def course_delete(request, pk):
    """Delete a course."""
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('crud:course_list')
    return render(request, 'crud/course_confirm_delete.html', {'course': course})


def instructor_list(request):
    """List all instructors."""
    instructors = Instructor.objects.all()
    return render(request, 'crud/instructor_list.html', {'instructors': instructors})


def instructor_create(request):
    """Create a new instructor."""
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:instructor_list')
    else:
        form = InstructorForm()
    return render(request, 'crud/instructor_form.html', {'form': form})


def instructor_update(request, pk):
    """Update an existing instructor."""
    instructor = get_object_or_404(Instructor, pk=pk)
    if request.method == 'POST':
        form = InstructorForm(request.POST, instance=instructor)
        if form.is_valid():
            form.save()
            return redirect('crud:instructor_list')
    else:
        form = InstructorForm(instance=instructor)
    return render(request, 'crud/instructor_form.html', {'form': form})


def instructor_delete(request, pk):
    """Delete an instructor."""
    instructor = get_object_or_404(Instructor, pk=pk)
    if request.method == 'POST':
        instructor.delete()
        return redirect('crud:instructor_list')
    return render(request, 'crud/instructor_confirm_delete.html', {'instructor': instructor})


def instructor_detail(request, pk):
    """Show instructor detail."""
    instructor = get_object_or_404(Instructor, pk=pk)
    return render(request, 'crud/instructor_detail.html', {'instructor': instructor})


def learner_list(request):
    """List all learners."""
    learners = Learner.objects.all()
    return render(
        request,
        'crud/learner_list.html',
        {'learners': learners}
    )


def learner_create(request):
    """Create a new learner."""
    if request.method == 'POST':
        form = LearnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:learner_list')
    else:
        form = LearnerForm()
    return render(request, 'crud/learner_form.html', {'form': form})


def learner_update(request, pk):
    """Update an existing learner."""
    learner = get_object_or_404(Learner, pk=pk)
    if request.method == 'POST':
        form = LearnerForm(request.POST, instance=learner)
        if form.is_valid():
            form.save()
            return redirect('crud:learner_list')
    else:
        form = LearnerForm(instance=learner)
    return render(request, 'crud/learner_form.html', {'form': form})

# Delete a learner
def learner_delete(request, pk):
    learner = get_object_or_404(Learner, pk=pk)
    if request.method == 'POST':
        learner.delete()
        return redirect('crud:learner_list')
    return render(request, 'crud/learner_confirm_delete.html', {'learner': learner})


# Learner detail view
def learner_detail(request, pk):
    learner = get_object_or_404(Learner, pk=pk)
    # Get courses the learner is enrolled in
    enrolled_courses = Course.objects.filter(
        enrollment__learner=learner
    ).distinct()
    return render(
        request,
        'crud/learner_detail.html',
        {
            'learner': learner,
            'enrolled_courses': enrolled_courses
        }
    )

# Course detail view
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(
        request, 'crud/course_detail.html', {'course': course}
    )
