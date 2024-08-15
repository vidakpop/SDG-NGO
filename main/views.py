from django.shortcuts import render,redirect
from .models import GalleryCategory,GalleryImage,Event
from django.utils import timezone

# Create your views here.

def home(request):
    
    images = GalleryImage.objects.all()
    categories=GalleryCategory.objects.all()
    # Fetch all active upcoming events
    upcoming_events = Event.objects.filter(is_active=True, date__gte=timezone.now()).order_by('date')

    # Fetch the most upcoming event (if any)
    most_upcoming_event = upcoming_events.first() if upcoming_events else None

    # Pass the events and the most upcoming event to the template
    context={'images':images,'categories':categories,'events': upcoming_events,
        'most_upcoming_event': most_upcoming_event,
        'most_upcoming_event_date': most_upcoming_event.date if most_upcoming_event else None}

    return render(request, 'home.html',context)

def about(request):
    return render(request, 'about.html', {})

def location(request):
    return render(request, 'location.html', {})

def gallery(request):
    return render(request, 'gallery.html', {})

def contact(request):
    return render(request, 'contact.html', {})

from django.http import JsonResponse

def event_list(request):
    # Fetch all active upcoming events
    upcoming_events = Event.objects.filter(is_active=True, date__gte=timezone.now()).order_by('date')

    # Fetch the most upcoming event (if any)
    most_upcoming_event = upcoming_events.first() if upcoming_events else None

    # Pass the events and the most upcoming event to the template
    context = {
        'events': upcoming_events,
        'most_upcoming_event': most_upcoming_event,
        'most_upcoming_event_date': most_upcoming_event.date if most_upcoming_event else None
    }
    
    return render(request, 'event.html', context)