from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='photos/', blank=True, null=True)
    image_name = models.CharField(max_length=50)
    image_caption = models.TextField()
    profile = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    likes = models.IntegerField(default=0)
    comments = models.TextField(default=0)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.image_name