from django.shortcuts import render, redirect
from apps.courses.models import Course
from apps.settings.models import Settings, Response
# Create your views here.
def course_index(request, id):
    settings = Settings.objects.latest('id')
    course = Course.objects.get(id = id)
    random_courses = Course.objects.all().order_by('?')[:2]
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        direction = course.title
        response = Response.objects.create(name = name, phone = phone, direction = direction)
        response.save()
        return redirect('course', course.id)
    context = {
        'setting': settings,
        'course' :course,
        'random_courses':random_courses,
    }
    return render(request, 'course_detail.html', context)