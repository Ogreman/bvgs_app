from django.views import generic
from django.http import HttpResponse

from .models import Event
from .forms import EventForm


class EventListView(generic.ListView):
    model = Event


class EventDetailView(generic.DetailView):
    model = Event


class EventCreateView(generic.CreateView):
    model = Event
    form = EventForm


class EventUpdateView(generic.UpdateView):
    model = Event
    form = EventForm