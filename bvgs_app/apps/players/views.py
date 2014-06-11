# Create your views here.
from django.views import generic
from django.http import HttpResponse

from .models import Player
from .forms import PlayerForm


class PlayerListView(generic.ListView):
    model = Player


class PlayerDetailView(generic.DetailView):
    model = Player


class PlayerCreateView(generic.CreateView):
    model = Player
    form = PlayerForm


class PlayerUpdateView(generic.UpdateView):
    model = Player
    form = PlayerForm