from django.contrib import admin

from .models import Event
from .forms import EventForm


class EventPlayerInline(admin.TabularInline):
    model = Event.attendees.through
    fields = ('player',)
    readonly_fields = ('exp_given',)


class EventAdmin(admin.ModelAdmin):
    form = EventForm
    inlines = [
        EventPlayerInline,
    ]

admin.site.register(Event, EventAdmin)