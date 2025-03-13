from django import forms
from .models import Location, Profile
from django.contrib.auth.models import User
from .widgets import CustomImageField

class UserForm(forms.ModelForm):
    username= forms.CharField(disabled=True)
    class Meta:
        model= User
        fields= ('username', 'first_name', 'last_name')

class ProfileForm(forms.ModelForm):
    photo= forms.ImageField(widget=CustomImageField)
    bio= forms.TextInput()
    class Meta:
        model= Profile 
        fields= ('photo', 'bio', 'phone_number')

class LocationForm(forms.ModelForm):
    class Meta:
        model= Location
        fields= {'address_1', 'address_2', 'city', 'department'}