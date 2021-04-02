from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from mapbox_location_field.models import LocationField, AddressAutoHiddenField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

CATEGORY_CHOICES = [
    ('action','Action'),
    ('drama','DRAMA'),
    ('comedy','COMEDY'),
    ('romance','ROMANCE'),
]

STATUS_CHOICES = [
    ('NOS','NOT ON SELL'),
    ('OS','ON SELL'),
] 
# Create your models here.
# location = LocationField()
    # user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
class Event(models.Model):
    name = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length =100)#tag de l'evemenemt
    category = models.CharField(max_length = 7, choices = CATEGORY_CHOICES, default = '1')
    description = RichTextUploadingField() 
    location = LocationField(
        map_attrs={"style": "mapbox://styles/mightysharky/cjwgnjzr004bu1dnpw8kzxa72", "center": (17.031645, 51.106715)})
    created_at = models.DateTimeField(auto_now_add=True)
    address = AddressAutoHiddenField()
    event_start_date = models.DateField(null=True, blank=True)#date de debut
    event_start_time = models.TimeField(null=True, blank=True)
    event_end_date = models.DateField(null=True, blank=True)#date de fin
    event_end_time = models.TimeField(null=True, blank=True)  
    images_baniere = models.ImageField(upload_to='img')
    images_2 = models.ImageField(upload_to='img')
    


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    maximum_attende = models.PositiveIntegerField()#nombre de place maximun
    price = models.IntegerField()
    ticket_cathegories = models.CharField(max_length = 15)
    ticket_start_date_sell = models.DateField(null=True, blank=True)#date de debut
    ticket_start_time_sell = models.TimeField(null=True, blank=True)
    ticket_end_date_sell = models.DateField(null=True, blank=True)#date de fin
    ticket_end_time_sell = models.TimeField(null=True, blank=True)
    min_ticket = models.IntegerField(default=1)
    max_ticket = models.IntegerField(default=10)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return str(self.ticket_cathegories)

class OrderEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

 