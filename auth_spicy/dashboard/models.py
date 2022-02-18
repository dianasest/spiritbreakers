from django.db import models
import geocoder

# Create your models here.


class Data(models.Model):
    country = models.CharField(max_length=100, null=True,blank=True, verbose_name="Адрес Банкомата")
    latitude = models.FloatField(default=0, null=True,blank=True)
    longitude = models.FloatField(default=0, null=True,blank=True)
    balance = models.IntegerField(default=10000)
    filled = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = 'Data'

    def save(self, *args, **kwargs):
        self.latitude = geocoder.osm(self.country).lat
        self.longitude = geocoder.osm(self.country).lng
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.country
