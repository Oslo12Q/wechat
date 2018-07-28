#!/usr/bin/env Python
# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import json
from .models import *

def index(request):
    return render(request,'search_name.html')

def get_json_response(request, json_rsp):
    return HttpResponse(json.dumps(json_rsp), content_type='application/json')


def search_name(request):
    
    pass