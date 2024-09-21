from django.core.management.base import BaseCommand
from faker import Faker
from account.models import User  

class Command(BaseCommand):
    help = 'Populate User table with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        existing_emails = set(User.objects.values_list('email', flat=True))  
        for _ in range(100):  
            email = fake.email()
            
            while email in existing_emails:
                email = fake.email()
            
            first_name = fake.first_name()
            last_name = fake.last_name()
            password = fake.password()  
            role = fake.random_element(elements=('student', 'teacher'))  
            User.objects.create_user(
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
                role=role
            )

            existing_emails.add(email) 

        self.stdout.write(self.style.SUCCESS('Successfully populated User records.'))
