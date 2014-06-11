from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['name', 'starts', 'ends', 'last_event', 'capacity', 'attendees']

