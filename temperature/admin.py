from django.contrib import admin
 
from .models import Reading, Sensor
 
admin.site.register(Reading)
admin.site.register(Sensor)