# Generated by Django 4.1.3 on 2022-11-26 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(verbose_name='Дата собтия'),
        ),
    ]