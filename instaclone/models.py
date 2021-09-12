from django.db import models
import datetime as dt
from django.contrib.auth.models import User
# Create your models here.


class Image(models.Model):
    image_name =models.CharField(max_length=60,blank=True)
    image_caption=models.CharField(max_length=60,blank=True)
    posted_On = models.DateTimeField(auto_now_add=True)
    profile =models.ForeignKey(User)
    user_profile=models.ForeignKey(Profile)
    image=models.ImageField(upload_to='images/',default="Image")


    def __str__(self):
        return self.image_name

class Profile:(models.Model):
    profile_pic=models.ImageField('photo')
    Bio=models.CharField(max_length=35)
    user= models.OneToOneField(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.user

