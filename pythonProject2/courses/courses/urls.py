from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),  # List all courses
    path('courses/<int:id>/', views.course_detail, name='course_detail'),  # View details of a specific course
    path('courses/create/', views.course_create, name='course_create'),  # Create a new course
    path('courses/<int:id>/update/', views.course_update, name='course_update'),  # Update a specific course
    path('courses/<int:id>/delete/', views.course_delete, name='course_delete'),  # Delete a specific course
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('student/<int:pk>/update/', views.student_update, name='student_update'),
    path('student/<int:pk>/delete/', views.student_delete, name='student_delete'),
]
