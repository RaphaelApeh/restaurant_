from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import User
import datetime

class Command(BaseCommand):

    def handle(self,*args,**kwargs):
        print(f'{kwargs}')
        print('hello world')