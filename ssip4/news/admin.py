from django import forms
from django.contrib import admin

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import NewsEntry


class NewsEntryAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = NewsEntry
        exclude = ['created']


class NewsEntryAdmin(admin.ModelAdmin):
    form = NewsEntryAdminForm
    list_display = ['title', 'created']

admin.site.register(NewsEntry, NewsEntryAdmin)
