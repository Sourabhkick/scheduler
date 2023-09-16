
from django.urls import path
from . import views

urlpatterns = [
    path('calendar/', views.calendar_view, name='calendar'),
    path('create/', views.create_event, name='create_event'),
]
