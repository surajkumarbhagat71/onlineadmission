from django.contrib import admin
from public.models import *
# Register your models here.

class PeoplesAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'contact',
        'secondary_contact',
        'city',
        'state',
        'street'
    ]


admin.site.register(Peoples,PeoplesAdmin)
admin.site.register(Categories)