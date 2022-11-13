from distutils.command.upload import upload
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15 , blank=True , null=True)
    photo = models.ImageField(upload_to='images/' , blank=True)

    def get_absolute_url(self):
        return reverse("profile", kwargs={"pk": self.pk})