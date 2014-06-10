# Create your views here.
from django.views.generic import View, ListView
from django.http import HttpResponse

from .models import Player

class SampleHomeView(View):
	def get(self, request, *args, **kwargs):
		return HttpResponse("Hello world")


class PlayerListView(ListView):
    model = Player