from django.contrib import admin
from service.models import service
# Register your models here.
@admin.register(service)
class adminservice(admin.ModelAdmin):
    list_display=('service_icon','service_title','service_des')

