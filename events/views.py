from django.shortcuts import render
from.models import Events


# Create your views here.
def home(request):
    events = Events.objects
    return render(request, 'events/home.html', {'events': events})
