from django.conf.urls import url

from . import views

urlpatterns = [
    #ex /queue
    url(r'^$', views.client_view, name='client_view'),
    #ex /queue/increment
    url(r'^increment$', views.increment_tail, name='increment_tail')
    ]
