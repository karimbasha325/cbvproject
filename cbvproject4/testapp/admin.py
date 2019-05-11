from django.contrib import admin
from testapp.models import Mobile

# Register your models here.
class MobileAdmin(admin.ModelAdmin):
    list_display=['brand','ram','camera','price']

admin.site.register(Mobile,MobileAdmin)
