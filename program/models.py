from django.db import models

# Create your models here.

class Program(models.Model):
       title = models.CharField(max_length=100)
   event_type = models.CharField(max_length=100, default='No Information')
   description = models.CharField(max_length=1024)
   entry_fee = models.CharField(max_length=512, default='No Information')
   website = models.CharField(max_length=512, default=None, blank=True, null=True)
   event_date = models.DateField()
   place = models.CharField(max_length=100)
   artiste = models.CharField(max_length=100)
   phone = models.CharField(max_length=15)
   event_start = models.TimeField()
   event_end = models.TimeField()
   duration = models.FloatField()
   location_address1 = models.CharField(max_length=512)
   location_address2 = models.CharField(max_length=512, default=None, blank=True, null=True)
   location_city = models.CharField(max_length=100)
   location_state = models.CharField(max_length=50)
   location_country = models.CharField(max_length=50, default=None, blank=True, null=True)
   location_pincode = models.CharField(max_length=10)
   location_mapcoords = models.CharField(max_length=100, default='0,0')
   location_parking = models.CharField(max_length=100, default='No Information')
   location_eataries = models.CharField(max_length=100, default='No Information')
   artiste_image = models.CharField(max_length=512, default='', blank=True, null=True)
