# Generated by Django 4.1.3 on 2022-11-28 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_graduates_reviews_response_response_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='logo',
            field=models.FileField(upload_to='logo/'),
        ),
    ]
