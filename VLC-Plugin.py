# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 02:25:37 2016
@author: archit08jain
"""

## define the label vs operation function
from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()

def fun(inp):
    if(inp==4):
        k.press_keys(k.space)
    elif(inp==3):
        k.press_key(k.alt_key)
        k.tap_key(k.right_key,n=8)
        k.release_key(k.alt_key)
    elif(inp==2):
        k.press_keys([k.windows_l_key,'d'])
    else:
        k.press_key(k.alt_key)
        k.tap_key(k.left_key,n=8)
        k.release_key(k.alt_key)


## passing the operation function to the server

from server import startApp

# make sure APPID doesnot collide with the existing APPID
APP_ID = "VLC MEDIA PLAYER PLUGIN"
#to launch the plugin specify the port number APPID and fun(label)
startApp(8000,APP_ID,fun)




    

        