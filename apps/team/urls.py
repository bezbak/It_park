from django.urls import path
from apps.team.views import  teacher

urlpatterns = [
    path('<int:id>/', teacher, name = 'teacher'),

]
