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

@login_required(login_url='accounts/login')
def photo_upload(request):
    current_user = request.user 
    if request.method =='POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.save()
        return redirect('/')
    
    else: 
        form = ImageForm()

    return render(request,"photo_upload.html",{"form":form})

@login_required(login_url='accounts/login')
def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()

        return redirect('/')
    else:
        form = ProfileForm()

    return  render(request,"create_profile.html",{'form':form})

def user_profile(request, username):
    username = request.user
    profiles = Profile.objects.all()

    return render(request,"profile.html", {"profiles":profiles})