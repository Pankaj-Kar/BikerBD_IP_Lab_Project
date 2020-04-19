from django.db import models

# Create your models here.
class eventlist(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to="events/images" ,default = "")
    time = models.CharField(max_length = 50)

    def __str__(self):
        return self.title