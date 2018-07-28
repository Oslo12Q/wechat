#!/usr/bin/env Python
# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from PIL import Image
import qrcode 
import time
import random

import traceback
import logging

def q_code(id):
    try:
        img = qrcode.make("http://liuzhiqiang.top/qr_code/qr_code/?qr_id="+id)

        #image_name = '{}_{}_{}.png'.format(id,long(time.time()), random.randint(1000, 9999))
        #desc_path = '/images/'+image_name
        #img.save(desc_path)
        buf = StringIO()
        img.save(buf)
        image_stream = buf.getvalue()
    
        
        return image_stream
    except Exception, err:
        logging.error(err)
        logging.error(traceback.format_exc())



        import qrcode
from cStringIO import StringIO
def ceshi(rewuest):
    img = qrcode.make('12')
 
    buf = StringIO()
    img.save(buf)
    image_stream = buf.getvalue()
 
    response = HttpResponse(image_stream, content_type="image/png")
    response['Last-Modified'] = 'Mon, 27 Apr 2015 02:05:03 GMT'
    response['Cache-Control'] = 'max-age=31536000'
    return response



    