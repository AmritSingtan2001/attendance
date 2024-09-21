from django.db import models
from account.models import User



class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)  

    def __str__(self):
        return f"{self.student.first_name} - {self.date}"


    class Meta:
        ordering =['-date']