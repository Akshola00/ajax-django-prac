from django.db import models

# Create your models here.
class table(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    