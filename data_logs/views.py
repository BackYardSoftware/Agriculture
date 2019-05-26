from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    """The home page for Learning Log."""
    return render(request, 'data_logs/index.html')
