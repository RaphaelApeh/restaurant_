from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
import uuid

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
    
class Food(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField(default=9.9)
    image = models.ImageField(upload_to='images')
    food_id = models.UUIDField(default=uuid.uuid4(),unique=True)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail',kwargs={'food_id':self.food_id})