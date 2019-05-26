from __future__ import unicode_literals
 
from django.db import models
 
class Sensor(models.Model):
    name = models.CharField(max_length = 200)
 
def __str__(self):
    return self.name
 
class Reading(models.Model):
    sensor = models.ForeignKey(Sensor,
    on_delete = models.CASCADE)
    time = models.DateTimeField('Time')
    value = models.IntegerField(default = 0)
 
def __str__(self):
    return str(self.time) + " " + str(self.value)