from django.contrib import admin
from .models import Company
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display=['Company_Name','Company_logo','Company_city']
admin.site.register(Company,CompanyAdmin)