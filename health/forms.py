from dataclasses import fields
import profile
from django import forms
from .models import profile
class Patientform():
    class Meta:
        model=profile
        fields= "__all__"