"""Script to read and display all courses from the database."""
# pylint: disable=wrong-import-position
# flake8: noqa: E402

# Django specific settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# Ensure settings are read
from django.core.wsgi import get_wsgi_application

get_wsgi_application()

from crud.models import Course

# Your code starts from here:

# Find all courses
courses = Course.objects.all()  # pylint: disable=no-member
print(courses)
