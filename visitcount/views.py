from django.shortcuts import render
from django.http import HttpResponse

from .models import VisitCounter

# Create your views here.

def show_number_of_visitors(request):
    record = VisitCounter.objects.all()[0]
    return HttpResponse("Current = %d" % record.counter)
