from django.contrib import admin

from .models import Authors, Books, Genres

admin.site.register((Authors, Books, Genres))