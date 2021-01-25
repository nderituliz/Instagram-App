from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Image, Profile
from .forms import ImageForm, ProfileForm

# Create your views here.
def home_page(request):
    current_user = request.user
    images = Image.objects.all()
    profile = Profile.objects.all()
    
    return render(request, "index.html",{'images':images})