from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings    
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)  
    phone_num=models.BigIntegerField(unique=True,blank=True,null=True)
    canCreateBlog = models.BooleanField(default=False)

class Blog(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date=models.DateTimeField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    date=models.DateTimeField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    def __str__(self):
        return self.content
    