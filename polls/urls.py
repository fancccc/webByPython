# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 11:52:38 2021

@author: Mario
"""

#from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('', views.index,name='index'),
]