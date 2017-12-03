from django.contrib import admin
from .models import Category, Tag, Video

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'video_number', 'number']
    fields = ['name', 'number', ]

class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'pub_date']

    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = (
            'admin/js/kindeditor/kindeditor-all.js',
            'admin/js/kindeditor/lang.zh_CN.js',
            'admin/js/kindeditor/config.js',
        )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Tag)
