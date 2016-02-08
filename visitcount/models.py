from django.db import models

# Create your models here.

class VisitCounter(models.Model):
    counter = models.IntegerField(default=0)

    def __str__(self):
        return str(self.counter)
    
    
