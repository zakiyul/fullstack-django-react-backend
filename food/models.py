from django.db import models
from django.db.models.deletion import CASCADE
from app.models import Chef

class FoodModel(models.Model):
  nama    = models.CharField(max_length=255)
  harga   = models.FloatField()
  chef    = models.ForeignKey(Chef, on_delete=models.CASCADE)
  gambar  = models.ImageField(upload_to='food/')

  def __str__(self):
      return self.nama
