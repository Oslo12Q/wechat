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
        img = qrcode.make("http://liuzhiqiang.top/oslo/?qr_id="+id)

        image_name = '{}_{}_{}.png'.format(id,long(time.time()), random.randint(1000, 9999))
        desc_path = '/images/'+image_name
        img.save(desc_path)
        return image_name
    except Exception, err:
        logging.error(err)
        logging.error(traceback.format_exc())


        
    