from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Promotor(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='promotor', on_delete=models.CASCADE)
    amount = models.IntegerField(max_length=255,blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
