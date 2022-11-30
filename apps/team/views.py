from django.shortcuts import render
from apps.team.models import Teacher
from apps.settings.models import Settings
# Create your views here.

def teacher(request, id):
    teacher = Teacher.objects.get(id = id)
    settings = Settings.objects.latest('id')
    context = {
        'setting' : settings,
        'teacher' : teacher
    }
    return render(request, 'teacher_detail.html', context)
