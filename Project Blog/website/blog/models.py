from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate,login,logout

# Create your models here.
class account(models.Model):
    type = models.CharField(max_length=100,blank=True,null=True)
    
    def __str__(self):
        return self.type

class User(AbstractUser):
    user_type = models.ForeignKey(account, on_delete=models.CASCADE,blank=True,null=True,related_name='user_status')

class account_confirmation(models.Model):
    user_acc = models.ForeignKey(account,on_delete=models.CASCADE,blank=True,null=True,related_name='identifier')
    user_code = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.user.type

class profile(models.Model):
    user_acc = models.OneToOneField(User,on_delete=models.CASCADE,related_name ='user_profile',blank=True,null=True)
    profile_pic = models.ImageField(upload_to='profile_image',blank=True,null=True)
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
