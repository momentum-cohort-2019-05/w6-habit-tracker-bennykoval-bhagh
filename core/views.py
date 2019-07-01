from django.shortcuts import render
from core.models import Habit, DailyRecord
from django.views import generic
# from django.views.generic import TemplateView
# Create your views here.

class HabitView(generic.ListView):
    model = Habit
    template_name = "index.html"