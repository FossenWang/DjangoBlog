from django.contrib import admin
from .models import Category, Tag, Video

class VideoInline(admin.TabularInline):
    model = Video
    fields = ['title', 'video', 'pub_date', 'author']
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name',]
    inlines = [VideoInline]

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'pub_date')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Tag)
