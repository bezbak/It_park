from django.contrib import admin
from apps.team.models import Teacher
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.

class TeacherAdminForm(forms.ModelForm):
    description = forms.CharField(label= 'Описание',widget=CKEditorUploadingWidget())
    class Meta:
        model = Teacher
        fields = '__all__'

class TeacherAdmin(admin.ModelAdmin):
    form = TeacherAdminForm

admin.site.register(Teacher, TeacherAdmin)