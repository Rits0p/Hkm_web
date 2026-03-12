from django.shortcuts import render, get_object_or_404
from .models import Event

def events_home(request):
    events = Event.objects.all().prefetch_related('images').order_by('-event_date')
    return render(request, 'pages/event.html', {'events': events})

def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    images = event.images.all()
    return render(request, 'pages/event_detail.html', {
        'event': event,
        'images': images
    })

