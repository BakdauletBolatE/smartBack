from django.shortcuts import render
from django.views.generic import DetailView
from .models import Workers

class WorkerDetail(DetailView):
    
    model = Workers
    context_object_name = 'worker'
    template_name = 'workapp/single.html'