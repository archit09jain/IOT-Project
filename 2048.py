# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 03:10:42 2016

@author: archit08jain
"""

## define the label vs operation function
from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()

def fun(inp):
    if(inp==2):
        k.press_key(k.right_key)
    elif(inp==3):
        k.press_key(k.up_key)
    else:
        k.press_key(k.left_key)

## passing the operation function to the server

from server import startApp

# make sure APPID doesnot collide with the existing APPID
APP_ID = "2048 Motion Plugin"
#to launch the plugin specify the port number APPID and fun(label)
startApp(8000,APP_ID,fun)




    

        