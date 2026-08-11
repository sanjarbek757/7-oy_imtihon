from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    telefon_raqami = models.CharField(max_length=20, blank=True, null=True)
    tugilgan_sana = models.DateField(blank=True, null=True)


class Retsept(models.Model):
    QIYINLIK_CHOICES = (
        ("oson", "Oson"),
        ("orta", "O'rta"),
        ("qiyin", "Qiyin"),
    )
    sarlavha = models.CharField(max_length=200)
    masalliqlar = models.TextField()
    pishirish_vaqti = models.IntegerField()
    qiyinlik_darajasi = models.CharField(max_length=20)
    egasi = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="retseptlar")