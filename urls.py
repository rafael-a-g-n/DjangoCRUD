from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('course_list', permanent=False)),
    path('admin/', admin.site.urls),
    path('', include(('crud.urls', 'crud'), namespace='crud')),
]
