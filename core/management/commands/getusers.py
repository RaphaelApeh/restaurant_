from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth.models import User

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('user_id',type=int,help='user id')

    def handle(self,*args,**kwargs):
        user_id = kwargs['user_id']

        try:
            user = User.objects.get(id=user_id)
            print(
                f'{user.username} >>> {user.date_joined.date()}'
            )
        except User.DoesNotExist:
            self.stdout.write('User DoesNotExist')