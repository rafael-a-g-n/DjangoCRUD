"""Script to read and query learners from the database."""
# pylint: disable=wrong-import-position
# flake8: noqa: E402

# Django specific settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# Ensure settings are read
from django.core.wsgi import get_wsgi_application

get_wsgi_application()

from crud.models import Learner

# Your code starts from here:

# Find students with last name "Smith"
learners_smith = Learner.objects.filter(last_name="Smith")  # pylint: disable=no-member
print("1. Find learners with last name `Smith`:")
print(learners_smith)
print("\n")
# Order by dob descending, and select the first two objects
learners = Learner.objects.order_by("-dob")[0:2]  # pylint: disable=no-member
print("2. Find top two youngest learners:")
print(learners)
