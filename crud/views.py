"""Views for CRUD app models."""

from datetime import datetime

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from crud.forms import CourseForm, EnrollmentForm, InstructorForm, LearnerForm
from crud.models import Course, Enrollment, Instructor, Learner


def homepage(request):
    """Homepage view for portfolio project."""
    return render(request, 'crud/homepage.html', {'year': datetime.now().year})


def enrollment_delete(request, pk):
    """Delete an enrollment and redirect to the course detail page."""
    enrollment = get_object_or_404(Enrollment, pk=pk)
    course_id = enrollment.course.id
    if request.method == 'POST':
        enrollment.delete()
        return redirect('crud:course_detail', pk=course_id)
    return render(
        request,
        'crud/enrollment_confirm_delete.html',
        {'enrollment': enrollment}
    )


def enrollment_update(request, pk):
    """Update an existing enrollment."""
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('crud:course_detail', pk=enrollment.course.pk)
    else:
        form = EnrollmentForm(instance=enrollment)
    cancel_url = reverse('crud:course_detail', kwargs={'pk': enrollment.course.pk})
    return render(
        request,
        'crud/enrollment_form.html',
        {'form': form, 'course': enrollment.course, 'cancel_url': cancel_url}
    )


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
    cancel_url = reverse('crud:course_detail', kwargs={'pk': course_id})
    return render(
        request,
        'crud/enrollment_form.html',
        {'form': form, 'course': course, 'cancel_url': cancel_url}
    )


def course_list(request):
    """List all courses."""
    courses = Course.objects.all()
    return render(
        request,
        'crud/course_list.html',
        {'courses': courses, 'year': datetime.now().year}
    )


def course_create(request):
    """Create a new course."""
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:course_list')
    else:
        form = CourseForm()
    return render(
        request,
        'crud/course_form.html',
        {'form': form, 'year': datetime.now().year}
    )


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
    return render(
        request,
        'crud/course_form.html',
        {'form': form, 'year': datetime.now().year}
    )


def course_delete(request, pk):
    """Delete a course."""
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('crud:course_list')
    return render(
        request,
        'crud/course_confirm_delete.html',
        {'course': course, 'year': datetime.now().year}
    )


def instructor_list(request):
    """List all instructors."""
    instructors = Instructor.objects.all()
    return render(
        request,
        'crud/instructor_list.html',
        {'instructors': instructors, 'year': datetime.now().year}
    )


def instructor_create(request):
    """Create a new instructor."""
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crud:instructor_list')
    else:
        form = InstructorForm()
    return render(
        request,
        'crud/instructor_form.html',
        {'form': form, 'year': datetime.now().year}
    )


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
    return render(
        request,
        'crud/instructor_form.html',
        {'form': form, 'year': datetime.now().year}
    )


def instructor_delete(request, pk):
    """Delete an instructor."""
    instructor = get_object_or_404(Instructor, pk=pk)
    if request.method == 'POST':
        instructor.delete()
        return redirect('crud:instructor_list')
    return render(
        request,
        'crud/instructor_confirm_delete.html',
        {'instructor': instructor, 'year': datetime.now().year}
    )


def instructor_detail(request, pk):
    """Show instructor detail."""
    instructor = get_object_or_404(Instructor, pk=pk)
    return render(
        request,
        'crud/instructor_detail.html',
        {'instructor': instructor, 'year': datetime.now().year}
    )


def learner_list(request):
    """List all learners."""
    learners = Learner.objects.all()
    return render(
        request,
        'crud/learner_list.html',
        {'learners': learners, 'year': datetime.now().year}
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
    return render(
        request,
        'crud/learner_form.html',
        {'form': form, 'year': datetime.now().year}
    )


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
    return render(
        request,
        'crud/learner_form.html',
        {'form': form, 'year': datetime.now().year}
    )


def learner_delete(request, pk):
    """Delete a learner."""
    learner = get_object_or_404(Learner, pk=pk)
    if request.method == 'POST':
        learner.delete()
        return redirect('crud:learner_list')
    return render(
        request,
        'crud/learner_confirm_delete.html',
        {'learner': learner, 'year': datetime.now().year}
    )


def learner_detail(request, pk):
    """Show details for a specific learner."""
    learner = get_object_or_404(Learner, pk=pk)
    enrolled_courses = Course.objects.filter(
        enrollment__learner=learner
    ).distinct()
    return render(
        request,
        'crud/learner_detail.html',
        {
            'learner': learner,
            'enrolled_courses': enrolled_courses,
            'year': datetime.now().year
        }
    )


def course_detail(request, pk):
    """Show details for a specific course."""
    course = get_object_or_404(Course, pk=pk)
    return render(
        request,
        'crud/course_detail.html',
        {'course': course, 'year': datetime.now().year}
    )
