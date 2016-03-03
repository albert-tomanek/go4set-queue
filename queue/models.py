from django.db import models

# Create your models here.

class Queue(models.Model):
    queue_start = models.IntegerField(default=0)

    def __str__(self):
        return str(self.queue_start)
    
    
