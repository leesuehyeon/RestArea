from django.contrib import admin
from .models import Info, Photo

class PhotoInline(admin.TabularInline):
    model = Photo

class InfoAdmin(admin.ModelAdmin):
    search_fields = ['restinfo']
    inlines = [PhotoInline, ]

admin.site.register(Info, InfoAdmin)