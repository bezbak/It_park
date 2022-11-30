from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from apps.courses.models import Course


class CourseAdminForm(forms.ModelForm):
    description = forms.CharField(label= 'Описание',widget=CKEditorUploadingWidget())
    class Meta:
        model = Course
        fields = '__all__'

class CourseAdmin(admin.ModelAdmin):
    form = CourseAdminForm

admin.site.register(Course, CourseAdmin)