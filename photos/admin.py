from django.contrib import admin
from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image', 'upload_date')


admin.site.register(Photo, PhotoAdmin)
