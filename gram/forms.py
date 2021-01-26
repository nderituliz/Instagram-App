from django import forms
from .models import Profile,Picture,Comments

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['user']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Picture
        exclude =[ 'profile_details', 'like_add', 'vote_score', 'num_vote_up', 'num_vote_down','profile',]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['image','user']