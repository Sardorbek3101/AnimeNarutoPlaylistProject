from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models

# Create your models here.
class SlideModel(models.Model):
    title = models.CharField(max_length=50,default='AnimeFan')
    img1 = models.ImageField(upload_to='slide/')
    name1 = models.CharField(max_length=50, default='AnimeFan')
    body1 = models.CharField(max_length=200, default='Этот слайд создан только для преданных фанатов аниме Наруто !')
    img2 = models.ImageField(upload_to='slide/')
    name2 = models.CharField(max_length=50 , default='AnimeFan')
    body2 = models.CharField(max_length=200 , default='Этот слайд создан только для преданных фанатов аниме Наруто !')
    img3 = models.ImageField(upload_to='slide/' , blank=True)
    name3 = models.CharField(max_length=50 , blank=True)
    body3 = models.CharField(max_length=200 , blank=True)
    img4 = models.ImageField(upload_to='slide/' , blank=True)
    name4 = models.CharField(max_length=50 , blank=True , default='AnimeFan')
    body4 = models.CharField(max_length=200 , blank=True)
    img5 = models.ImageField(upload_to='slide/' , blank=True)
    name5 = models.CharField(max_length=50 , blank=True)
    body5 = models.CharField(max_length=200 , blank=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("slide_detail", kwargs={"pk": self.pk})
    