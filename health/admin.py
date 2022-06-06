from django.contrib import admin
from .models import symptoms,Usersymptoms
# Register your models here.


class symptomsad(admin.ModelAdmin):
    list_display = ('pk','symptom_name')

class usersymp_ad(admin.ModelAdmin):
    list_display=('pk','check_up_id','user')

admin.site.register(symptoms,symptomsad)
admin.site.register(Usersymptoms,usersymp_ad)