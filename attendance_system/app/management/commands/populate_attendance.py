
import random
from django.core.management.base import BaseCommand
from faker import Faker
from app.models import Attendance, User 

class Command(BaseCommand):
    help = 'Populate Attendance table with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(20): 
            student = random.choice(User.objects.filter(role="student"))  
            date = fake.date_between(start_date='-1y', end_date='today') 
            is_present = random.choice([True, False])  

            Attendance.objects.create(
                student=student,
                date=date,
                is_present=is_present
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Attendance records.'))
