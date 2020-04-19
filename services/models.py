

# Create your models here.
from django.db import models
from django.contrib.auth.models import User




class Service(models.Model):
    title = models.CharField(max_length=200, unique=True)
    place = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('service-detail', kwargs={'pk': self.pk})