from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
import datetime

# Create your models here.

class Habit(models.Model):
    """Model representing a habit"""
    goal = models.TextField(max_length=1000, help_text="Enter your daily goal here.")
    action = models.TextField(max_length=100, default="Test")
    quantity = models.PositiveIntegerField(default=1)
    item = models.TextField(max_length=100, default="Test")
    date = models.DateField(auto_now_add=True)  
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='user_habits')

    class Meta:
        ordering = ["-date"]
    
    def __str__(self):
        return self.goal

    def get_absolute_url(self):
        return reverse('habit-detail', args=[str(self.id)])

class DailyRecord(models.Model):
    description = models.TextField(max_length=500)
    quantity = models.PositiveIntegerField(default=1)
    date = models.DateField(auto_now_add=True)
    habit = models.ForeignKey(to=Habit, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["-date"]
    
    def __str__(self):
        return self.description


    
    
