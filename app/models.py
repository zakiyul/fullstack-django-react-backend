from django.db import models

class Chef(models.Model):
  GENDER = (
    ('lk','Laki-laki'),
    ('pr','Perempuan')
  )
  nama    = models.CharField(max_length=255)
  umur    = models.IntegerField()
  gender  = models.CharField(max_length=10, choices=GENDER)
  foto    = models.ImageField(upload_to='chef/')
  show    = models.BooleanField(default=True)

  def __str__(self):
    return self.nama