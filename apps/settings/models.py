from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=50)
    logo = models.FileField(upload_to='logo/')
    phone = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    facebook = models.URLField(verbose_name="Facebook", max_length=50, blank = True, null = True)
    instagram = models.URLField(verbose_name=("instagram"), max_length=50, blank = True, null = True)
    telegram = models.CharField(verbose_name=("telegram"), max_length=50, blank = True, null = True)
    facebook = models.URLField(verbose_name=("facebook"), max_length=50, blank = True, null = True)
    
    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'
        
class News(models.Model):
    image = models.ImageField(upload_to='news_iamges/')
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    date = models.DateTimeField("Дата собтия", auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        
class Response(models.Model):
    name = models.CharField("Имя заявки", max_length=50)
    phone = models.CharField("Номер заявки", max_length=50)
    direction = models.CharField("Направление заявки", max_length=50)
    response_status = models.BooleanField("Статус заявки", default=False)
    
    def __str__(self):
        return f'Имя {self.name}, номер {self.phone}, направление {self.direction}'
    
    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'
        
class Reviews(models.Model):
    name = models.CharField("Имя", max_length=50)
    text = models.CharField("Текст отзыва", max_length=255)
    image = models.ImageField('Фото выпусника', upload_to='review_iamge/')
    date = models.DateTimeField("Дата отзыва", auto_now_add=True)
    course = models.CharField("Курс отзыва", max_length=255)

    class Meta:
        verbose_name = ("Отзыв выпусника")
        verbose_name_plural = ("Отзывы выпусников")

    def __str__(self):
        return self.name
    
class Gallery(models.Model):
    photo = models.FileField(upload_to='gallery/')
    
    class Meta:
        verbose_name = ("Галларея")
        verbose_name_plural = ("Галларея")

    def __str__(self):
        return f'Photo {self.id}'

class About_us(models.Model):
    text = models.TextField(max_length=None)