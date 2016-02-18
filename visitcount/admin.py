from django.contrib import admin

# Register your models here.
from .models import VisitCounter

admin.site.register(VisitCounter)
