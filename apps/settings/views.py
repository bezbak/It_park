from django.shortcuts import render, redirect
from apps.settings.models import Settings, News, Response, Reviews, Gallery, About_us
from apps.courses.models import Course
from apps.team.models import Teacher
# Create your views here.
def index(request):
    setting = Settings.objects.latest('id')
    news = News.objects.order_by("-id")[0:5]
    reviews = Reviews.objects.all()
    gallery = Gallery.objects.all()
    courses = Course.objects.all()
    context = {
        'setting': setting,
        'news': news,
        'reviews': reviews,
        'courses': courses,
        'gallery':gallery
    }
    return render(request, 'index.html', context)

def news_detail(request, id):
    setting = Settings.objects.latest('id')
    news = News.objects.get(id = id)
    context = {
        'setting':setting,
        'news':news
    }
    return render(request, 'news_detail.html', context)

def test(request):
    course1 = Course.objects.get(title ='Frontend') 
    course2 = Course.objects.get(title ='Backend') 
    if request.method == 'POST':
        name = request.POST.get('name')
        first_ask = request.POST.get('first_ask')
        second_ask = request.POST.get('second_ask')
        age = request.POST.get('age')
        third_ask = request.POST.get('third_ask')
        if first_ask == 'Да' and second_ask =='Делать дизайн' or first_ask == 'Да' and third_ask == 'Нет':
            return redirect('course', course1.id)
        else:
            return redirect('course', course2.id)
            
    return render(request, 'test.html')

def about_us(request):
    setting = Settings.objects.latest('id')
    about_us = About_us.objects.latest('id')
    teacher = Teacher.objects.all()
    context = {
        'setting': setting,
        'about_us': about_us,
        'teacher': teacher,
    }
    return render(request, 'about.html', context)
# def get_review(request):
#     setting = Settings.objects.latest('id')
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         text = request.POST.get('text')
#         review = Reviews.objects.create(name = name, text = text)
#         review.save()
#         return redirect('index')
#     context = {     
#         'setting': setting,
#     }
#     return render(request, 'reviews.html', context)

def get_response(request):
    setting = Settings.objects.latest('id')
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        direction = request.POST.get('direction')
        response = Response.objects.create(name = name, phone = phone, direction = direction)
        response.save()
        return redirect('index')
    context = {
        'setting': setting,
    }
    return render(request, 'response.html', context)