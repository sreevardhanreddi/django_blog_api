import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'prints out environment variables'

    def handle(self, *args, **kwargs):
        for env in os.environ.items():
            print(env)
        
