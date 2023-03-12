from django.contrib import admin

# Register your models here.

from .models import Post, Comment

from .models import Photo, Category

admin.site.register(Post)
admin.site.register(Comment)

admin.site.register(Category)   # pridanie modelu do admin panela t.j.
admin.site.register(Photo)      # povie sa Djangu ktore modely ma vlozit na stranku
