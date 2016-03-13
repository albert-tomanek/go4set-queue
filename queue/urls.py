from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    #ex /queue
    url(r'^$', views.client_view, name='client_view'),
    #ex /queue
    url(r'^staff$', views.staff_view, name='staff_view'),

    #ex /queue/remove_from_queue
    url(r'^remove_from_queue$', views.remove_from_queue, name='remove_from_queue'), 
    
    #ex /queue/increment_head
    url(r'^increment_head$', views.increment_head, name='increment_head'),
    #ex /queue/increment_tail
    url(r'^increment_tail$', views.increment_tail, name='increment_tail'),
    #ex /queue/reset
    url(r'^reset$', views.reset, name='reset'),
    ]
