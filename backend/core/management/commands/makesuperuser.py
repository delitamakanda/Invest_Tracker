from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Creates a superuser with a random username and password'
    def handle(self, *args, **kwargs):
        username = 'admin'
        email = 'admin@example.com'
        password = get_random_string(length=10)
        try:
            u = None
            if not User.objects.filter(username=username).exists():
                u = User.objects.create_superuser(username, email, password)
                self.stdout.write(self.style.SUCCESS(f'Superuser created: {username}'))
                self.stdout.write(self.style.SUCCESS(f'Password: {password}'))
                self.stdout.write(self.style.SUCCESS(f'Email: {email}'))
            else:
                self.stdout.write(self.style.WARNING(f'Superuser {username} already exists.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(str(e))) # gokmf0J6Nt