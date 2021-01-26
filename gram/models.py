from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from vote.models import VoteModel
from vote.managers import VotableManager
# Create your models here.

    
class Profile(models.Model):
    photo = models.ImageField(upload_to='images', blank =True, null = True)
    Bio = models.TextField(max_length=1500)
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    
    def __str__(self):
        return self.Bio
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
        
    @classmethod
    def update_bio(cls,id,bio):
        update_profile = cls.objects.filter(id = id).update(bio =bio)
        return update_profile
    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile
    
    @classmethod
    def search_user(cls,user):
        return cls.objects.filter(user__username__icontains = user).all()
        
class Picture(VoteModel,models.Model):
    image = models.ImageField(upload_to = 'images/',blank = False, null = True)
    name = models.CharField(max_length = 100)
    caption = models.CharField(max_length = 100)
    profile = models.ForeignKey(User,on_delete = models.CASCADE)
    like_add = models.IntegerField(default=0)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    # comments = models.CharField(max_length = 1500)
    
    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    @classmethod
    def update_caption(self,caption):
        updated_cap = cls.objects.filter(id = id).update(caption = caption)
        return updated_cap
    
    @classmethod
    def get_all_images(cls):
        image = cls.objects.all()
        return image
    
    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id= id).all()
        return image
    
    @classmethod
    def search_by_profile(cls,name):
        profile = Profile.objects.filter(user__name__icontains = name)
        return profile
    
    @classmethod
    def get_one_image(cls,id):
        image = cls.objects.get(id = id)
        return image
    
    
    
    class Meta:
        ordering = ['-date_uploaded']
    
class Comments(models.Model):
    comment = models.CharField(max_length = 50, blank=True)
    posted = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey(Picture, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()
        
        
    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter(image__id=id)
        return comments


    def __str__(self):
        return self.comment
    
class Likes(models.Model):
    image = models.ForeignKey(Picture, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_likes(self):
        self.save()

    def delete_like(self):
        self.delete()

    def count_likes(self):
        likes = self.likes.count()
        return likes