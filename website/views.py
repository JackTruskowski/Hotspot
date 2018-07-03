# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.template import loader
from .models import Sample
from .models import RestaurantNaive
# Create your views here.

from django.http import HttpResponse

def index(request):
    #latest_sample_data = Sample.objects.all()
    #template = loader.get_template('website/index.html')
    #context = {
    #    'latest_sample_data':
    #    latest_sample_data,
    #}
    latest_rest_data=RestaurantNaive.objects.all()[:10]
    template = loader.get_template('website/index.html')
    context = {
        'latest_rest_data':
        latest_rest_data,
    }
        
    
    return HttpResponse(template.render(context, request))


