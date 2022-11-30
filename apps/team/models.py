from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField("Имя учителя", max_length=50)
    direction = models.CharField("Курс учителя", max_length=50)
    description = models.CharField("Об учителе", max_length=500)
    image = models.ImageField("Фотография учителя" ,upload_to='team_iamges/', )
    video = models.FileField("Видео учителя" ,upload_to='team_videos/', )
    facebook = models.URLField(verbose_name="Facebook", max_length=50, blank = True, null = True)
    instagram = models.URLField(verbose_name=("instagram"), max_length=50, blank = True, null = True)
    telegram = models.CharField(verbose_name=("telegram"), max_length=50, blank = True, null = True)
    whatsapp = models.CharField(verbose_name=("whatsapp"), max_length=50, blank = True, null = True)
    

    class Meta:
        verbose_name = ("Учитель")
        verbose_name_plural = ("Учителя")

    def __str__(self):
        return self.name
