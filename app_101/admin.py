from django.contrib import admin

from app_101.models import Person

admin.site.site_header = "Umoja Sacco"
admin.site.site_title = "Umoja Sacco Admin Portal"
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'email' ,'phone' ,'gender']
    list_filter= ['gender']
    search_fields = ['name' , 'email' , 'phone' , 'dob']
admin.site.register(Person , PersonAdmin)