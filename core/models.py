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
    
class Order(models.Model):
    food = models.ForeignKey(Food,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.food.name} ~ {self.full_name}'


class Profile(models.Model):
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    foods = models.ManyToManyField(Food,blank=True)

    def __str__(self):
        return self.user.username