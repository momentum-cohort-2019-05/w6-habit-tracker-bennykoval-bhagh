from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='habits/', permanent=True)),
    path('habits/', views.HabitView.as_view(), name='habit'),
]

