from django.contrib import admin
from django import forms
from .models import Review, Photo

class PhotoInline(admin.TabularInline):
    model = Photo

class ReviewAdmin(admin.ModelAdmin):
    search_fields = ['restreview']
    inlines = [PhotoInline, ]

admin.site.register(Review, ReviewAdmin)