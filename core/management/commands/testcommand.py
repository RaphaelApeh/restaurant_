from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import User
import datetime

class Command(BaseCommand):

    def handle(self,*args,**kwargs):
        today = datetime.date.today()
        users = User.objects.filter(is_active=False)
        for x in users:
            start = x.date_joined.date()
            end = start + datetime.timedelta(minutes=60)
            if end < today:
                x.delete()
                print(f'{x.username}')