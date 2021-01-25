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