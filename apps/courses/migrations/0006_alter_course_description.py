# Generated by Django 4.1.3 on 2022-11-29 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_rename_dscription_course_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=255, verbose_name='Описание курса'),
        ),
    ]