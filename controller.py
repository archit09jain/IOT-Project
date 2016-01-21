from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()


def fun(inp):
    if(inp==4):
        k.tap_key(k.right_key,n = 3)        
        #k.press_keys(['s',k.right_key])
    elif(inp==3):
        #k.press_key(k.alt_key)
        #k.tap_key(k.right_key,n=8)
        #k.release_key(k.alt_key)
        x_dim, y_dim = m.screen_size()
        m.click(x_dim/2, y_dim/2, 1)
    elif(inp==2):
        k.press_keys([k.windows_l_key,'d'])
    elif(inp==5):
        k.tap_key(k.left_key)
    elif(inp==6):
        k.tap_key(k.up_key)
    elif(inp==7):
        k.tap_key(k.down_key)
    else:
        k.press_key(k.alt_key)
        k.tap_key(k.left_key,n=8)
        k.release_key(k.alt_key)
    

        

