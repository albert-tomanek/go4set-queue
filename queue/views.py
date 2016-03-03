from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Queue

# Create your views here.

def show_number_of_visitors(request):
    record = Queue.objects.all()[0]
    
    template = loader.get_template('queue/counter.html')
    
    context = {
        'queue_start' : record.queue_start
        }
    
    return HttpResponse(template.render(context, request))

def increment_counter(request):
    record = Queue.objects.all()[0]   # This is the valur from the database

    record.queue_start += 1     # We add one to it,
    
    record.save()   # And then we save it.
    
    #
    return HttpResponseRedirect( reverse('queue:number-of-visitors') )
