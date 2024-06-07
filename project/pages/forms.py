from django import forms
from .models import Admins,User,Department,UserhasDep,AdminsHasDep

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','Password','e_mail']

class AdminsForm(forms.ModelForm):
    class Meta:
        model = Admins
        fields = ['UserName','Password']