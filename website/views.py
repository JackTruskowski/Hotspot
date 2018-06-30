# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.template import loader
from .models import Sample
# Create your views here.

from django.http import HttpResponse

def index(request):
    latest_sample_data = Sample.objects.all()
    template = loader.get_template('website/index.html')
    context = {
        'latest_sample_data':
        latest_sample_data,
    }
    return HttpResponse(template.render(context, request))


