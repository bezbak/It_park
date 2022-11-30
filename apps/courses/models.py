from django.db import models
from apps.team.models import Teacher
# Create your models here.
class Course(models.Model):
    title = models.CharField(("Название курса"), max_length=50)
    description = models.CharField(("Описание курса"), max_length=1000)
    price = models.CharField(("Цена курса"), max_length=50)
    image = models.FileField(("Постер курса"),upload_to="course_iamges/")
    video = models.FileField(("Видео курса"),upload_to="course_video/", blank=True, null=True)
    teacher = models.ForeignKey(Teacher,verbose_name='Учитель курса', on_delete=models.DO_NOTHING, related_name='course_teacher')
    support = models.ForeignKey(Teacher,verbose_name='Саппрт курса', on_delete=models.DO_NOTHING, related_name='course_support')

    class Meta:
        verbose_name = ("Курс")
        verbose_name_plural = ("Курсы")

    def __str__(self):
        return self.title