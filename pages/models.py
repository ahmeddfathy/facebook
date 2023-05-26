from django.db import models


class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username

# Create your models here.
