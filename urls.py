"""Project URL configuration for DjangoCRUD."""

from django.contrib import admin
from django.urls import path, include


from crud import views as crud_views

urlpatterns = [
    path('', crud_views.homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('', include(('crud.urls', 'crud'), namespace='crud')),
]
