import phone
from django import forms

from app_101.models import Person


class PersonForm(forms.ModelForm):
    gender = forms.ChoiceField(choices={('Male', 'Male'), ('Female', 'Female')}, widget=forms.RadioSelect)

    class Meta:
        model = Person
        fields = ['name', 'email', 'phone', 'dob', 'weight', 'height', 'gender','salary','profile_pic']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date', 'min':'1900-01-01', 'max':'2025-12-31'}),
        'weight': forms.NumberInput(attrs={'type': 'number', 'min': 20, 'max': 120}),
        'height': forms.NumberInput(attrs={'type': 'number', 'min': 1.4, 'max': 2.5}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', max_length=20, widget=forms.PasswordInput())
