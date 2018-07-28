#!/usr/bin/env Python
# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from django.shortcuts import render_to_response,render
from django.http import HttpResponse, JsonResponse

def mp_verify(request):
    return HttpResponse('PNyE15nlc1gky07l', content_type="text/plain;charset=UTF-8")

def oslo(request):
    return HttpResponse('Whatever is worth doing is worth doing wel', content_type="text/plain;charset=UTF-8")

def love(request):
   return render(request,'love.html')


def xln(request):
   return HttpResponse('星光不问赶路人 时光不负有心人',content_type="text/plain;charset=UTF-8")
