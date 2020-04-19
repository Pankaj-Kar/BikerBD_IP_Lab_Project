from django.shortcuts import render
from django.http import HttpResponse
from .models import eventlist
# Create your views here.
def events(request):
    list = eventlist.objects.all()
    return render(request, "events/event_list.html", {'evnt':list})
