from django.contrib import admin
from .models import Category, Tag, Video

admin.site.register([Category, Tag, Video])
