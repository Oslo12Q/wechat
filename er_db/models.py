#!/usr/bin/env Python
# coding=utf-8
from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Mob_User(models.Model):
    name = models.CharField('姓名',max_length=255, blank=True, null=True)
    sex = models.CharField('性别',max_length=255, blank=True, null=True)
    date_of_birth= models.CharField('出生日期',max_length=255, blank=True, null=True)
    certificate_no = models.CharField('证书编号',max_length=255, blank=True, null=True)
    id_card = models.CharField('身份证号',max_length=255, blank=True, null=True)
    professional_level = models.CharField('职业（工种）及等级',max_length=255, blank=True, null=True)
    results_1 = models.IntegerField('理论知识考试成绩',blank=True, null=True)
    results_2 = models.IntegerField('操作技能考核成绩',blank=True, null=True)
    assess = models.CharField('评定成绩',max_length=255, blank=True, null=True)
    date = models.CharField('颁证日期',max_length=255, blank=True, null=True)
    unit = models.CharField('发证单位',max_length=255, blank=True, null=True)
    unit_no = models.CharField('证书流水码所属号段',max_length=255, blank=True, null=True)
    create_time = models.DateTimeField('创建时间')
    update_time = models.DateTimeField('更新时间')

    def __unicode__(self):
    	return self.name
    class Meta:
        verbose_name = 'Mob_User'
        verbose_name_plural='The user details'

    