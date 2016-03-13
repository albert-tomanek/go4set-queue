from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import permission_required
from django.contrib.sessions.models import Session
from .models import Queue

# Create your views here.

def client_view(request):
    record = Queue.objects.all()[0]
    
    template = loader.get_template('queue/client.html')

    queue_position = request.session['queue_position'] if ( 'queue_position' in request.session ) else None
    
    context = {
        'queue_head' : record.head,
        'queue_tail' : record.tail,

        'queue_position' : queue_position  # Actually a cookie
        }
    
    return HttpResponse(template.render(context, request))

@permission_required('queue.can_admin')
def staff_view(request):
    record = Queue.objects.all()[0]
    
    template = loader.get_template('queue/staff.html')
    
    context = {
        'queue_head' : record.head,
        'queue_tail' : record.tail
        }
    
    return HttpResponse(template.render(context, request))

@permission_required('queue.can_admin')
def increment_head(request):
    record = Queue.objects.all()[0]   # This is the value from the database

    record.head += 1     # We add one to it,
    
    record.save()   # And then we save it.
    
    #
    return HttpResponseRedirect( reverse('queue:staff_view') )

def increment_tail(request):
    record = Queue.objects.all()[0]   # This is the value from the database

    record.tail += 1     # We add one to it,
    record.save()   # And then we save it.

    request.session['queue_position'] = record.tail
    
    #
    return HttpResponseRedirect( reverse('queue:client_view') )

def reset(request):
    record = Queue.objects.all()[0]   # This is the value from the database

    record.head = 0
    record.tail = 0
    
    record.save()   # And then we save it.

    Session.objects.all().delete() # Delete all the sessions (like cookies)
    
    #
    return HttpResponseRedirect( reverse('queue:staff_view') )


