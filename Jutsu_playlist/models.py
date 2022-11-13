from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models
# Create your models here.
class PlaylistJutsuModel(models.Model):
    photo = models.ImageField(upload_to='jut_img/')
    name = models.CharField(max_length=50)
    about = models.TextField()
    ninja = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("jutsu_detail", kwargs={"pk": self.pk})