from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Mobile(models.Model):
    brand=models.CharField(max_length=100)
    ram=models.CharField(max_length=100)
    camera=models.CharField(max_length=100)
    price=models.IntegerField()

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
