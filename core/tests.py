from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Food,Category
User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.testuser = User.objects.create_user('testuser','testuser@gmail.com','passworduser')
    def test_user_password(self):
        test_user = self.testuser.check_password('passworduser')
        self.assertTrue(test_user)
    def test_user_count(self):
        pass
