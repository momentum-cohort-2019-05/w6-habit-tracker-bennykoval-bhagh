from django.shortcuts import render
from django.views.generic import TemplateView

from core.models import Habit, DailyRecord
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404


# from django.views.generic import TemplateView
# Create your views here.

class HabitView(TemplateView):
    model = Habit
    template_name = "index.html"

    def get_context_data(self, **kwargs):
         context = super(HabitView, self).get_context_data(**kwargs)
         context['habit'] = Habit.objects.all()
         return context
  



class HabitDetailView(generic.DetailView):
    model = Habit
    template_name = "habit_detail.html"

class CreateDailyRecord(LoginRequiredMixin, CreateView):
    model = DailyRecord
    template_name = "dailyrecord_form.html"

    fields = ['description', 'quantity']


    def get_context_data(self, **kwargs):
        context = super(CreateDailyRecord, self).get_context_data(**kwargs)
        context['habit'] = get_object_or_404(Habit, pk = self.kwargs['pk'])
        return context
    
    def form_valid(self, form):
        form.instance.habit=get_object_or_404(Habit, pk = self.kwargs['pk'])
        return super(CreateDailyRecord, self).form_valid(form)

    def get_success_url(self): 
        return reverse('habit-detail', kwargs={'pk': self.kwargs['pk'],})