from django.conf.urls import url

from . import views

urlpatterns = [
    #ex /queue
    url(r'^$', views.show_number_of_visitors, name='number-of-visitors'),
    #ex /queue/increment
    url(r'^increment$', views.increment_counter, name='increment')
    ]
