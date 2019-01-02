from django.contrib import admin
from rangoapp.models import Category, Page, UserProfile


# Register your models here.
admin.site.register(Category)

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
#region 第二种写法
# class PageAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'url')


# admin.site.register(Page, PageAdmin)
#endregion

admin.site.register(UserProfile)
