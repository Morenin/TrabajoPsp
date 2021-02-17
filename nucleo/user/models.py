from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    Dni = models.CharField(max_length=9, verbose_name='Dni')

    def save(self,*args,**kwargs):
        if self.pk is None:
            self.set_password(self.password)
        super().save(*args,**kwargs)
    
    
        