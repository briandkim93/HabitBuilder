from django.db import models
from django.contrib.auth.models import User

class Day(models.Model):
    day = models.CharField(max_length=3)
    def __str__(self):
        return self.day

class DateCompleted(models.Model):
    date_completed = models.DateField()
    def __str__(self):
        return str(self.date_completed)

class Habit(models.Model):
    habit = models.CharField(max_length=70)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    days = models.ManyToManyField(Day)
    date_created = models.DateField()
    dates_completed = models.ManyToManyField(DateCompleted)
    def __str__(self):
        return self.habit