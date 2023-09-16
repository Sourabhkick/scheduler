
from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm

def calendar_view(request):
    events = Event.objects.all()
    return render(request, 'scheduler/calendar.html', {'events': events})

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar')
    else:
        form = EventForm()
    return render(request, 'scheduler/create_event.html', {'form': form})

