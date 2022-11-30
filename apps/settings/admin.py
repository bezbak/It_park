from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from apps.settings.models import Settings, News, Response, Reviews,  Gallery, About_us
# Register your models here.
admin.site.register(Settings)
admin.site.register(Response)
admin.site.register(News)
admin.site.register(Reviews)
admin.site.register(Gallery)


class About_usAdminForm(forms.ModelForm):
    text = forms.CharField(label= 'Описание',widget=CKEditorUploadingWidget())
    class Meta:
        model = About_us
        fields = '__all__'

class About_usAdmin(admin.ModelAdmin):
    form = About_usAdminForm

admin.site.register(About_us, About_usAdmin)