from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.conf.urls import url


urlpatterns = [
    path('', RedirectView.as_view(url='goals/', permanent=True)),
    path('goals/', views.HabitView.as_view(), name='habit'),
    path('goals/<int:pk>', views.HabitDetailView.as_view(), name='habit-detail'),
    path('goals/<int:pk>/dailyrecord/', views.CreateDailyRecord.as_view(), name='dailyrecord_form'),
    path('goals/new/', views.habit_new, name='new'),
    url(r'^register/', views.register, name='register'),
]

