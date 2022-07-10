from django.db import models


# Create your models here.
class Events(models.Model):
    event_img = models.ImageField(upload_to='event_images/')
    event_text = models.CharField(max_length=300)
