from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    colour = models.CharField(max_length=50, null=True)
    year = models.CharField(max_length=50, null=True)
    image1 = models.ImageField(upload_to='villa', null=True)
    image2 = models.ImageField(upload_to='villa', null=True, blank=True)
    image3 = models.ImageField(upload_to='villa', null=True, blank=True)
    def __str__(self):
        return f"{self.name}"


