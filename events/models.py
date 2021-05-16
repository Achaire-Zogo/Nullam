from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from mapbox_location_field.models import LocationField, AddressAutoHiddenField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
# model import
from accounts.models import Promotor

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
class Cathegorie(models.Model):
    name = models.CharField(max_length = 10, choices = CATEGORY_CHOICES, default = '1')
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

class Event(models.Model):
    promotor = models.ForeignKey(Promotor, related_name='eventss', on_delete=models.CASCADE)
    category = models.ForeignKey(Cathegorie, related_name='eventss', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255)
    tag = models.CharField(max_length =100)#tag de l'evemenemt
    description = RichTextUploadingField()
    location = models.CharField(max_length=255)
    event_start_date = models.DateField(null=True, blank=True)#date de debut
    event_start_time = models.TimeField(null=True, blank=True)
    event_end_date = models.DateField(null=True, blank=True)#date de fin
    event_end_time = models.TimeField(null=True, blank=True)  
    date_added = models.DateTimeField(auto_now_add=True)
    images_baniere = models.ImageField(upload_to='img')
    images_2 = models.ImageField(upload_to='img')

    class Meta:
        ordering = ['-date_added']
    

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    # auto generating the slug
    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Event.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
    # saving the slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

class Ticket(models.Model):
    event = models.ForeignKey(Event, related_name='tickets', on_delete=models.CASCADE)
    promotor = models.ForeignKey(Promotor, related_name='tickets', on_delete=models.CASCADE)
    maximum_attende = models.PositiveIntegerField()#nombre de place maximun
    price = models.IntegerField()
    ticket_cathegories = models.CharField(max_length = 15)
    slug = models.SlugField(max_length=255)
    ticket_start_date_sell = models.DateField(null=True, blank=True)#date de debut
    ticket_start_time_sell = models.TimeField(null=True, blank=True)
    ticket_end_date_sell = models.DateField(null=True, blank=True)#date de fin
    ticket_end_time_sell = models.TimeField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    min_ticket = models.IntegerField(default=1)
    max_ticket = models.IntegerField(default=10)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return str(self.ticket_cathegories)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.ticket_cathegories)
        canvas = Image.new('RGB', (290,290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.ticket_cathegories}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname,File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)


class Publish(models.Model):
    event = models.ForeignKey(Event, related_name='publishs', on_delete=models.CASCADE)
    promotor = models.ForeignKey(Promotor, related_name='publishs', on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, related_name='publishs', on_delete=models.CASCADE)
    publish_date = models.DateField(null=True, blank=True)#date de publication


class OrderEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

 