from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Event(models.Model):
    titre = models.CharField(max_length=50)
    description = models.TextField()
    photo = models.ImageField(upload_to='img')
    price = models.IntegerField()
    discount_price = models.IntegerField()

    def __str__(self):
        return self.titre


class OrderEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
