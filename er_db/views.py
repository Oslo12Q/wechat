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
import qrcode
from cStringIO import StringIO


'''
    # 搜索页面
'''
def index(request):
    return render(request,'search_name.html')

def destical(request):
    return render(request,'destical.html')

def err_destical(request):
    return render(request,'err_destical.html')


def oc_img(request):
    try:
        id = request.GET.get('id',None)
        mob = Mob_User.objects.filter(id = id)
        if not mob:
            return get_json_response(request, dict(suc_id=0, ret_cd=104, ret_ts=long(time.time()),errorMsg = 'err',successResult='',im = ''))
        img = qrcode.make("http://liuzhiqiang.top:8020/qr_code/oslo/?qr_id="+id)

        buf = StringIO()
        img.save(buf)
        image_stream = buf.getvalue()
    
        response = HttpResponse(image_stream, content_type="image/png")
        response['Last-Modified'] = 'Mon, 27 Apr 2015 02:05:03 GMT'
        response['Cache-Control'] = 'max-age=31536000'
        return response
    except Exception, err:
        logging.error(err)
        logging.error(traceback.format_exc())

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



import traceback
import logging
# 搜索名字API POST  参数：name
def search_name(request):
    try:
        if request.method != 'POST': # 必须POST 请求 负责返回 Method not allowed
            return get_json_response(request, dict(suc_id=0, ret_cd=405, ret_ts=long(time.time()),errorMsg = 'Method not allowed',successResult='',im = ''))

        name = request.POST.get('name',None)    
        print name
        if not name:  
            return get_json_response(request, dict(suc_id=0, ret_cd=104, ret_ts=long(time.time()),errorMsg = 'Please upload parameters name',successResult='',im = ''))
        
        mob = Mob_User.objects.filter(name = name)
        if not mob:
            return get_json_response(request, dict(suc_id=0, ret_cd=104, ret_ts=long(time.time()),errorMsg = 'Not name',successResult='',im = ''))
        
        for arr_mob in mob:
            id = arr_mob.id
            print id    
        return get_json_response(request, dict(suc_id=1, ret_cd=200, ret_ts=long(time.time()),errorMsg = '',successResult='',im = id))
    except Exception, err:
        logging.error(err)
        logging.error(traceback.format_exc())
        return get_json_response(request, dict(suc_id=1, ret_cd=500, ret_ts=long(time.time()),errorMsg = 'err',successResult='',im = ''))


def qr_code(request):
    try:
        arr_data = []
        #if request.method != 'POST': # 必须POST 请求 负责返回 Method not allowed
        #    return get_json_response(request, dict(suc_id=0, ret_cd=405, ret_ts=long(time.time()),errorMsg = 'Method not allowed',successResult='',im = ''))

        qr_id = request.GET.get('qr_id',None)
        if not qr_id:
            return get_json_response(request, dict(suc_id=0, ret_cd=104, ret_ts=long(time.time()),errorMsg = 'Please upload parameters name',successResult='',im = ''))
        mob = Mob_User.objects.filter(id = qr_id)
        if not mob:
            return get_json_response(request, dict(suc_id=0, ret_cd=104, ret_ts=long(time.time()),errorMsg = 'err',successResult='',im = ''))
        for i in mob:
            name = i.name
            sex = i.sex
            date_of_birth = i.date_of_birth
            certificate_no = i.certificate_no
            id_card = i.id_card
            professional_level = i.professional_level
            results_1 = i.results_1
            results_2 = i.results_2
            assess = i.assess
            date = i.date
            unit = i.unit
            unit_no = i.unit_no
            arr_list = {
                'name':name,'sex':sex,'date_of_birth':date_of_birth,'certificate_no':certificate_no,
                'id_card':id_card,'professional_level':professional_level,'results_1':results_1,'results_2':results_2,
                'assess':assess,'date':date,'unit':unit,'unit_no':unit_no
            }
            arr_data.append(arr_list)
        
        return get_json_response(request, dict(suc_id=1, ret_cd=200, ret_ts=long(time.time()),errorMsg = '',successResult=arr_data,im = ''))
    except Exception, err:
        logging.error(err)
        logging.error(traceback.format_exc())
        return get_json_response(request, dict(suc_id=1, ret_cd=500, ret_ts=long(time.time()),errorMsg = 'err',successResult='',im = ''))


