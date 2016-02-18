from django.conf.urls import url

from . import views

urlpatterns = [
    #ex /visitcount
    url(r'^$', views.show_number_of_visitors, name='number-of-visitors')
    ]
