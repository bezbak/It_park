# Generated by Django 4.1.3 on 2022-11-28 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
        ('courses', '0003_alter_course_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='support',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='course_support', to='team.teacher', verbose_name='Саппрт курса'),
            preserve_default=False,
        ),
    ]
