from django.contrib import admin
from News.models import News
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','desc')

admin.site.register(News,NewsAdmin)
