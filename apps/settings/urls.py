from django.urls import path
from apps.settings.views import index, get_response, news_detail, test, about_us
urlpatterns = [
    path('', index, name = 'index'),
    path('response/', get_response, name = 'response'),
    path('test/', test, name = 'test'),
    path('news/<int:id>/', news_detail, name = 'news_detail'),
    path('about_us/', about_us, name = 'about'),
]