from django.contrib import admin

from .models import Player
from .forms import PlayerForm


class PlayerAdmin(admin.ModelAdmin):
    form = PlayerForm
    readonly_fields = ['level', 'exp', 'multiplier', 'created', 'modified']
    list_display = ('name', 'level', 'exp', 'created')

admin.site.register(Player, PlayerAdmin)