#!/usr/bin/env Python
# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from django.shortcuts import render_to_response,render
from django.http import HttpResponse, JsonResponse



def oslo(request):
   return HttpResponse('星光不问赶路人 时光不负有心人',content_type="text/plain;charset=UTF-8")
