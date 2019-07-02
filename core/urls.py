from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='habits/', permanent=True)),
    path('habits/', views.HabitView.as_view(), name='habit'),
    path('habits/<int:pk>', views.HabitDetailView.as_view(), name='habit-detail'),
    path('habits/<int:pk>/dailyrecord/', views.CreateDailyRecord.as_view(), name='dailyrecord_form'),
    path('habits/new/', views.habit_new, name='new'),

]

