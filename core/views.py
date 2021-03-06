from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import HabitForm
from core.models import Habit, DailyRecord
from django.views import generic
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import re


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

    fields = ['quantity']

    def get_context_data(self, **kwargs):
        context = super(CreateDailyRecord, self).get_context_data(**kwargs)
        context['habit'] = get_object_or_404(Habit, pk = self.kwargs['pk'])
        return context
    
    def form_valid(self, form):
        form.instance.habit=get_object_or_404(Habit, pk = self.kwargs['pk'])
        return super(CreateDailyRecord, self).form_valid(form)

    def get_success_url(self): 
        return reverse('habit-detail', kwargs={'pk': self.kwargs['pk'],})

def habit_new(request):
    if request.method == "POST":
        form = HabitForm(request.POST)
        if form.is_valid():
            numbers =[]
            post = form.save(commit=False)
            data = request.POST.copy()
            
            pulldata = data.get('goal')
            rawdata = str(pulldata)
            rawdata = rawdata.replace(',', '')
            matches = re.findall("(\d+)", rawdata)

            post.user = request.user
            post.quantity = int(matches[0]) 
            
            post.save()
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = HabitForm()
    return render(request, 'habit_new.html', {'form': form})

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request, 'registration/reg_form.html', args)
        
