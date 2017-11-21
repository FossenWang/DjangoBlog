from django.contrib import admin

from .models import Category, Tag, Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):

    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = (
            'admin/js/kindeditor/kindeditor-all.js',
            'admin/js/kindeditor/lang.zh_CN.js',
            'admin/js/kindeditor/config.js',
        )

admin.site.register(Post, admin_class=PostAdmin)
admin.site.register([Tag, Category, Comment])
