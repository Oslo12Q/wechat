#!/usr/bin/env Python
# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import json
import time
import datetime
from .models import *

'''
    # 搜索页面
'''
def index(request):
    return render(request,'search_name.html')

# json时间处理
class DateEncoder(json.JSONEncoder):  
    def default(self, obj):  
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')   
        elif isinstance(obj,date):
            return obj.strftime('%Y-%m-%d')
        else:    
            return json.JSONEncoder.default(self, obj) 


# 通用函数,返回json数据
def get_json_response(request, json_rsp):
    return HttpResponse(json.dumps(json_rsp,cls=DateEncoder), content_type='application/json')


# 搜索名字API POST  参数：name
def search_name(request):
    if request.method != 'POST': # 必须POST 请求 负责返回 Method not allowed
        return get_json_response(request, dict(suc_id=0, ret_cd=405, ret_ts=long(time.time()),errorMsg = 'Method not allowed',successResult='',im = ''))

    name = request.POST.get('name',None)    
    if not name:  
        return get_json_response(request, dict(suc_id=0, ret_cd=104, ret_ts=long(time.time()),errorMsg = 'Please upload parameters name',successResult='',im = ''))
    
    mob = Mob_User.objects.filter(name = name)
    if not mob:
        return get_json_response(request, dict(suc_id=0, ret_cd=104, ret_ts=long(time.time()),errorMsg = 'Not name',successResult='',im = ''))
    
    for arr_mob in mob:
        id = arr_mob.id

    pass


def qr_code(request):
    qr_id = request.GET.get('qr_id',None)
    if not qr_id:
        return get_json_response(request, dict(suc_id=0, ret_cd=104, ret_ts=long(time.time()),errorMsg = 'Please upload parameters name',successResult='',im = ''))
    