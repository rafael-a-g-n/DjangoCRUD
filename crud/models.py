"""Django models for the CRUD application."""

from django.db import models
from django.utils.timezone import now


# Define your models from here:
# User model
class User(models.Model):
    """Represents a user with basic information."""

    first_name = models.CharField(null=False, max_length=30, default="john")
    last_name = models.CharField(null=False, max_length=30, default="doe")
    email = models.EmailField(null=False, max_length=50, default="john.doe@example.com")
    location = models.CharField(null=True, max_length=100, default="Unknown")
    dob = models.DateField(null=True)

    # Create a toString method for object string representation
    def __str__(self):
        return self.first_name + " " + self.last_name


# Instructor model
class Instructor(User):
    """Represents an instructor who is a type of user with additional teaching
    information."""

    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField()

    # Create a toString method for object string representation
    def __str__(self):
        return (
            "First name: "
            + self.first_name
            + ", "
            + "Last name: "
            + self.last_name
            + ", "
            + "Is full time: "
            + str(self.full_time)
            + ", "
            + "Total Learners: "
            + str(self.total_learners)
        )

    # Learner modelclass Learner(User):


class Learner(User):
    """Represents a learner who is a type of user with additional learning
    information."""

    STUDENT = "student"
    DEVELOPER = "developer"
    DATA_SCIENTIST = "data_scientist"
    DATABASE_ADMIN = "dba"

    OCCUPATION_CHOICES = [
        (STUDENT, "Student"),
        (DEVELOPER, "Developer"),
        (DATA_SCIENTIST, "Data Scientist"),
        (DATABASE_ADMIN, "Database Admin"),
    ]

    occupation = models.CharField(
        null=False,
        max_length=20,
        choices=OCCUPATION_CHOICES,
        default=STUDENT,
    )
    social_link = models.URLField(max_length=200)

    # Create a toString method for object string representation
    def __str__(self):
        return (
            "First name: "
            + self.first_name
            + ", "
            + "Last name: "
            + self.last_name
            + ", "
            + "Occupation: "
            + self.occupation
            + ", "
            + "Social Link: "
            + self.social_link
        )


# Course model
class Course(models.Model):
    """Represents a course that can be taught by multiple instructors."""

    name = models.CharField(null=False, max_length=100, default="online course")
    description = models.CharField(max_length=500)
    # Many-To-Many relationship with Instructor
    instructors = models.ManyToManyField(Instructor)
    # Many-To-Many relationship with Learner via Enrollment relationship
    learners = models.ManyToManyField(Learner, through="Enrollment")

    # Create a toString method for object string representation
    def __str__(self):
        return "Name: " + self.name + "," + "Description: " + self.description


# Enrollment model as a lookup table with additional enrollment info
class Enrollment(models.Model):
    """Represents the enrollment of a learner in a course with additional
    information."""

    AUDIT = "audit"
    HONOR = "honor"
    COURSE_MODES = [
        (AUDIT, "Audit"),
        (HONOR, "Honor"),
    ]
    # Add a learner foreign key
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    # Add a course foreign key
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Enrollment date
    date_enrolled = models.DateField(default=now)
    # Enrollment mode
    mode = models.CharField(max_length=5, choices=COURSE_MODES, default=AUDIT)


# Lesson
class Lesson(models.Model):
    """Represents a lesson that belongs to a course."""

    title = models.CharField(max_length=200, default="title")
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    content = models.TextField()
