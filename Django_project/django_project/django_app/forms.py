from django import forms
from .models import User

class UserForm(forms.Form):
    Employee = forms.ModelChoiceField(queryset=User.objects.all(), label="Select Employee")
