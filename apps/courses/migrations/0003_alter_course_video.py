# Generated by Django 4.1.3 on 2022-11-28 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_video_alter_course_dscription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='course_video/', verbose_name='Видео курса'),
        ),
    ]
