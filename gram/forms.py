from django import forms
from .models import Image, Profile

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image','image_name','image_caption','profile','likes','comments']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        #exclude = ['username']
        fields = ['profile', 'bio']