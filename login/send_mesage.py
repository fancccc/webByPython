# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 14:19:25 2022

@author: 20277
"""

import smtplib
from email.message import EmailMessage
import time

def send(text):
    try:
        msg = EmailMessage()
        msg.set_content('%s\n(FROM CentOs8 %s)'%(text,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))
        # me == the sender's email address
        # you == the recipient's email address
        msg['Subject'] = 'The New Log of My Server'
        msg['From'] = 'workfc@163.com'
        msg['To'] = 'workfc@163.com'
        # Send the message via our own SMTP server.
        #s = smtplib.SMTP('smtp.163.com')
        s = smtplib.SMTP_SSL('smtp.163.com', 465)
        s.login('workfc@163.com','FGYERUZNXGDZMFZK') 
        s.send_message(msg)
        s.quit()
    except Exception as e:
        print(e)
        send(text)
    
    return True

def main(n, filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    if n != len(data):
        res = ''.join(data[n:len(data)])
        return len(data), res
    else:
        return n, ''

if __name__ == '__main__':
    filename = 'nohup.out'
    with open(filename, 'r') as f:
        n = len(f.readlines())
    while True:
        m, res = main(n, filename)
        if m != n:
            send(res)
            n = m
        time.sleep(60*20)


        
    
    
        
        