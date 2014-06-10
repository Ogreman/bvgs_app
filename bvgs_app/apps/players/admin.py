from django.contrib import admin

from .models import Player
from .forms import PlayerCreateForm


class PlayerAdmin(admin.ModelAdmin):
    form = PlayerCreateForm
    readonly_fields = ['level', 'exp', 'multiplier']
admin.site.register(Player, PlayerAdmin)