from django import forms
from .models import Profile, Project, Comment
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['bio','profile_picture'] 
        exclude=['user','projects','contact']  

