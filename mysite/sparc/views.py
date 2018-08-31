# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def sparc(request):
        return render(request, 'sparc.html')

def polls1(request):
        return render(request, 'polls1.html')

def iconnect(request):
        return render(request, 'iconnect.html')

