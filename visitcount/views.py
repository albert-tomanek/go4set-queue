from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import VisitCounter

# Create your views here.

def show_number_of_visitors(request):
    record = VisitCounter.objects.all()[0]
    
    template = loader.get_template('visitcount/counter.html')
    
    context = {
        'counter' : record.counter
        }
    
    return HttpResponse(template.render(context, request))
