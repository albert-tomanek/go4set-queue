from django.db import models

# Create your models here.

class Queue(models.Model):
    head = models.IntegerField(default=0)
    tail = models.IntegerField(default=0)

    def __str__(self):
        return str(self.tail)
    
    
