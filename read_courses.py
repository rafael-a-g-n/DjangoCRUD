# Django specific settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# Ensure settings are read
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

from crud.models import *

# Your code starts from here:

# Find all courses
courses = Course.objects.all()
print(courses)
