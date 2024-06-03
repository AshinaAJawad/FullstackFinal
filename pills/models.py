from django.db import models
from django.contrib.auth.models import User
from datetime import date 
class Medicine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dose = models.IntegerField()
    days = models.CharField(max_length=200)
    time = models.TimeField()

    def is_reminder_due_today(self):
        return date.today() in self.days
    
    def __str__(self):
        return self.name

