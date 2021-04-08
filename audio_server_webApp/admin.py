from django.contrib import admin
from .models import song, podcast, audiobook

admin.site.register(song)
admin.site.register(podcast)
admin.site.register(audiobook)

# Register your models here.

