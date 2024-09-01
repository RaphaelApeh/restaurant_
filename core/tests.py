from django.test import TestCase,Client
from django.contrib.auth import get_user_model

from .models import Food,Category
User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.testuser = User.objects.create_user('testuser','testuser@gmail.com','passworduser')
    def test_user_password(self):
        test_user = self.testuser.check_password('passworduser')
        self.assertTrue(test_user)

class FoodTestCase(TestCase):
    def setUp(self):
        test_category = Category.objects.create(name='Test',image='test.png')
        category = test_category
        self.food = Food.objects.create(
            category=category,
            name='test',
            image='bg.png',)

    def test_food_exists(self):
        qs = Food.objects.all()
        self.assertTrue(qs.exists())

# class ViewTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()

    # def test_home_template(self):
    #     path = self.client.get('/')
    #     self.assertTemplateUsed(request,'index.html')