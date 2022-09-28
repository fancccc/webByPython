# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 16:38:33 2021

@author: Mario
"""

from django.shortcuts import render
from django.views.decorators import csrf

# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "fanc.html", ctx)
