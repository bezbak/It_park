from django.urls import path
from apps.courses.views import course_index

urlpatterns = [
    path('<int:id>/', course_index, name = 'course'),
]
