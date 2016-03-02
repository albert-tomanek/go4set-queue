from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import VisitCounter

# Create your views here.

def show_number_of_visitors(request):
    record = VisitCounter.objects.all()[0]
    
    template = loader.get_template('visitcount/counter.html')
    
    context = {
        'counter' : record.counter
        }
    
    return HttpResponse(template.render(context, request))

def increment_counter(request):
    record = VisitCounter.objects.all()[0]   # This is the valur from the database

    record.counter += 1     # We add one to it,
    
    record.save()   # And then we save it.
    
    #
    return HttpResponseRedirect( reverse('visitcount:number-of-visitors') )
