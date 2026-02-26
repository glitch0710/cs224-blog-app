from django.contrib import admin
from .models import Post, Album, Song

# Register your models here.
admin.site.register(Post)
admin.site.register(Album)
admin.site.register(Song)