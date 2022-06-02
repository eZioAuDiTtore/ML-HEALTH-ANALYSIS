from django.contrib import admin
from .models import symptoms,Usersymptoms
# Register your models here.


class symptomsad(admin.ModelAdmin):
    list_display = ('pk','symptom_name')

admin.site.register(symptoms,symptomsad)
admin.site.register(Usersymptoms)