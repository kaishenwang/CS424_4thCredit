import socket  
from getkey import getkey, keys
# addr: ifconfig, en0, inet  
address = ('127.0.0.1', 31500)  
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
  
while True:  
    msg = ""
    key = getkey()
    if key == keys.UP:
        msg = "u"   
    elif key == keys.LEFT:
        msg = "l"
    elif key == keys.RIGHT:
        msg = "r"
    elif key == keys.DOWN:
        msg = "d"
    elif key == 'q':
        msg = "q"
        break 
    s.sendto(msg, address)  
  
s.close() 