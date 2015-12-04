from django.db import models

# Create your models here.

class Program(models.Model):
   title = models.CharField(max_length=100)
   description = models.CharField(max_length=1024)
   event_date = models.DateField()
   place = models.CharField(max_length=100)
   phone = models.CharField(max_length=15)
   event_start = models.TimeField()
   event_end = models.TimeField()
   duration = models.FloatField()
   location_address = models.CharField(max_length=512)
   location_mapcoords = models.CharField(max_length=100)
   location_parking = models.CharField(max_length=100)
   location_eataries = models.CharField(max_length=100)
   image = models.ImageField('Label', upload_to='path/')
