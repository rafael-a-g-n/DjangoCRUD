from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list, name='course_list'),
    path('courses/create/', views.course_create, name='course_create'),
    path('courses/<int:pk>/edit/', views.course_update, name='course_update'),
    path('courses/<int:pk>/delete/', views.course_delete, name='course_delete'),
    path('instructors/', views.instructor_list, name='instructor_list'),
    path('instructors/create/', views.instructor_create, name='instructor_create'),
    path('instructors/<int:pk>/edit/', views.instructor_update, name='instructor_update'),
    path('instructors/<int:pk>/delete/', views.instructor_delete, name='instructor_delete'),
    path('learners/', views.learner_list, name='learner_list'),
    path('learners/create/', views.learner_create, name='learner_create'),
    path('learners/<int:pk>/edit/', views.learner_update, name='learner_update'),
    path('learners/<int:pk>/delete/', views.learner_delete, name='learner_delete'),
]
