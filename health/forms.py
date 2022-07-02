from dataclasses import fields
from email.policy import default
from django import forms
from .models import Profile
choices_bld=(('A+ve','A+ve'),('A-ve','A-ve'),('B+ve','B+ve'),('B-ve','B-ve'),('AB+ve','AB+ve'),('AB-ve','AB-ve'),('O+ve','O+ve'),('O-ve','0-ve'))

class DateInput(forms.DateInput):
    input_type = 'date'
class Patientform(forms.ModelForm):
    blood_grp=forms.ChoiceField(choices=choices_bld)
    class Meta:
        model=Profile
        fields= ['p_id','phone','fname','lname','sex','dob','height','weight','blood_grp']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'})
        }

            
            
            
            