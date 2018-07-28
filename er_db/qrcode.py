from PIL import Image
import qrcode
import time
import random

import traceback
import logging

def q_code(id):
    try:
        qr = qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=1)

        qr.add_data("http://liuzhiqiang.top/oslo/?qr_id="+id)
        qr.make(fit=True)

        img = qr.make_image()
        img = img.convert("RGBA")

        icon = Image.open("20180728165514.jpg.png") #用于填充的图片 

        img_w, img_h = img.size
        factor = 4
        size_w = int(img_w / factor)
        size_h = int(img_h / factor)

        icon_w, icon_h = icon.size
        if icon_w > size_w:
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h
        icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

        w = int((img_w - icon_w) / 2)
        h = int((img_h - icon_h) / 2)
        img.paste(icon, (w, h), icon)

        image_name = '{}_{}_{}.jpg'.format(id,long(time.time()), random.randint(1000, 9999))
        desc_path = '/images/+'image_name
        img.save(desc_path)
        return image_name
    except Exception, err:
        logging.error(err)
        logging.error(traceback.format_exc())
    