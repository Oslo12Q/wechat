#!/usr/bin/env Python
# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from django.contrib import admin

# Register your models here.

from .models import *

class The_UserAdmin(admin.ModelAdmin):
    list_display=('name', 'sex', 'date_of_birth','certificate_no','id_card','professional_level','results_1','results_2','assess')
    search_fields = ('name',)
    list_per_page = 20
    ordering = ('-create_time',)
    list_display_links = ('name', 'sex', 'date_of_birth','certificate_no','id_card','professional_level','results_1','results_2','assess')
    #list_filter = ('is_custom',)
    #list_editable = ['name', 'tel_no']

admin.site.site_header = '国家职业资格证书管理系统'
admin.site.site_title = '国家职业资格证书管理系统'
admin.site.register(Mob_User,The_UserAdmin)