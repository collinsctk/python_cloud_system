#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from django.http import HttpResponseRedirect
from cloud_system.modules.vSphere.vsphere_0_vc_basic_actions import poweroff_vm_by_name, poweron_vm_by_name
from cloud_system.modules.vSphere.vsphere_0_login_info import vcip
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required


@login_required()
def poweroff(request, vmname):
    poweroff_vm_by_name(vcip, vmname)
    return HttpResponseRedirect('/myvms/')


@login_required()
def poweron(request, vmname):
    poweron_vm_by_name(vcip, vmname)
    return HttpResponseRedirect('/myvms/')