"""Script to write data to the database (create instructors, learners, courses)."""
# pylint: disable=wrong-import-position
# flake8: noqa: E402

# Django specific settings
import os
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# Ensure settings are read
from django.core.wsgi import get_wsgi_application

get_wsgi_application()

from crud.models import Course, Enrollment, Instructor, Learner, Lesson, User


# Your code starts from here:
def write_instructors():
    """Create and save instructor records to the database."""
    # Add instructors
    # Create a user
    user_john = User(first_name="John", last_name="Doe", dob=date(1962, 7, 16))
    user_john.save()
    instructor_john = Instructor(full_time=True, total_learners=30050)
    # Update the user reference of instructor_john to be user_john
    instructor_john.user = user_john
    instructor_john.save()

    instructor_yan = Instructor(
        first_name="Yan",
        last_name="Luo",
        dob=date(1962, 7, 16),
        full_time=True,
        total_learners=30050,
    )
    instructor_yan.save()

    instructor_joy = Instructor(
        first_name="Joy",
        last_name="Li",
        dob=date(1992, 1, 2),
        full_time=False,
        total_learners=10040,
    )
    instructor_joy.save()
    instructor_peter = Instructor(
        first_name="Peter",
        last_name="Chen",
        dob=date(1982, 5, 2),
        full_time=True,
        total_learners=2002,
    )
    instructor_peter.save()
    print("Instructor objects all saved... ")


def write_courses():
    """Create and save course records to the database."""
    # Add Courses
    course_cloud_app = Course(
        name="Cloud Application Development with Database",
        description="Develop and deploy application on cloud",
    )
    course_cloud_app.save()
    course_python = Course(
        name="Introduction to Python",
        description="Learn core concepts of Python and obtain hands-on "
        "experience via a capstone project",
    )
    course_python.save()

    print("Course objects all saved... ")


def write_lessons():
    """Create and save lesson records to the database."""
    # Add lessons
    lession1 = Lesson(title="Lesson 1", content="Object-relational mapping project")
    lession1.save()
    lession2 = Lesson(title="Lesson 2", content="Django full stack project")
    lession2.save()
    print("Lesson objects all saved... ")


def write_learners():
    """Create and save learner records to the database."""
    # Add learners
    learner_james = Learner(
        first_name="James",
        last_name="Smith",
        dob=date(1995, 3, 15),
        occupation=Learner.STUDENT,
        social_link="http://www.james.com",
    )
    learner_james.save()

    learner_maria = Learner(
        first_name="Maria",
        last_name="Garcia",
        dob=date(1988, 4, 20),
        occupation=Learner.DEVELOPER,
        social_link="http://www.maria.com",
    )
    learner_maria.save()

    learner_anthony = Learner(
        first_name="Anthony",
        last_name="Davidson",
        dob=date(1983, 3, 28),
        occupation=Learner.DATABASE_ADMIN,
        social_link="http://www.anthony.com",
    )
    learner_anthony.save()

    learner_mark = Learner(
        first_name="Mark",
        last_name="Taylor",
        dob=date(1987, 8, 26),
        occupation=Learner.DATA_SCIENTIST,
        social_link="http://www.mark.com",
    )
    learner_mark.save()
    print("Learner objects all saved... ")


def clean_data():
    """Delete all data to start from fresh."""
    # Delete all data to start from fresh
    Enrollment.objects.all().delete()  # pylint: disable=no-member
    User.objects.all().delete()  # pylint: disable=no-member
    Learner.objects.all().delete()  # pylint: disable=no-member
    Instructor.objects.all().delete()  # pylint: disable=no-member
    Course.objects.all().delete()  # pylint: disable=no-member
    Lesson.objects.all().delete()  # pylint: disable=no-member
    print("All data deleted... ")


# Clean any existing data first
clean_data()
write_courses()
write_instructors()
write_lessons()
write_learners()
