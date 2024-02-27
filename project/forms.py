from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput, EmailInput
from .models import user
from import_export import resources, fields

# Register a User
class CreateUserForm(UserCreationForm):
    first_name =  forms.CharField(required=True, max_length=20)
    last_name =  forms.CharField(required=True, max_length=20)
    matric_number =  forms.CharField(required=True, max_length=13)
    class Meta:
        model = User 
        fields = ['first_name','last_name','username', 'matric_number',  'password1', 'password2']

# CLASS USER

# User Login
class LoginFormuser(AuthenticationForm):
   
    # matric_number = forms.CharField(widget=TextInput())
    # username = forms.CharField(widget=TextInput())
    # email = forms.CharField(widget=EmailInput())
    # password = forms.CharField(widget=PasswordInput())
    class Meta:
         model = user
         fields = ['username','password']


# Create Record
class CreateuserForm(forms.ModelForm): 
    matric_number = forms.CharField(widget=TextInput())
    class Meta:
         model = user
         fields = ['first_name','last_name', 'matric_number', 'course', 'status', 'score']

# Update Record
class UpdateuserForm(forms.ModelForm): 

    class Meta:
         model = user
         fields = ['first_name', 'last_name', 'matric_number', 'course', 'status', 'score']

# import_export
         
class import_data(forms.Form):
    file = forms.FileField()
    class Meta:
        model = user
        fields= ['first_name', 'last_name', 'matric_number', 'course', 'status', 'score']

