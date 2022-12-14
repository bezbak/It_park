# Generated by Django 4.1.3 on 2022-11-27 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя учителя')),
                ('direction', models.CharField(max_length=50, verbose_name='Курс учителя')),
                ('image', models.ImageField(upload_to='team_iamges/', verbose_name='Фотография учителя')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
            },
        ),
    ]
