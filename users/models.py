from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bike = models.CharField(max_length=30, default = '')
    image = models.ImageField(upload_to = 'users/images', default="")
    bio = models.CharField(max_length = 200, default = "")
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    