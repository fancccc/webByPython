# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 21:05:51 2021

@author: Mario
"""

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    #return ["Hello World"] # python2
    return [b"Hello World"] # python3