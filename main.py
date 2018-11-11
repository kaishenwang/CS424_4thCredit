import serial
import time
import socket  
from getkey import getkey, keys

# this is the port you're connecting to the irobot with
# on windows, this is something like COM2
N = 2

OPCODE_DRIVE = 137
VELOCITY_SECOND = 90
VELOCITY_FIRST = 0

StraightList = [137, 0, 90, 0, 0x8000]
LeftList = [137, 0, 150, 0, 0xFFFF]
RighttList = [137, 0, 150, 0, 0x0001]

def ints2str(lst):
    '''
    Taking a list of notes/lengths, convert it to a string
    '''
    s = ""
    for i in lst:
        if i < 0 or i > 255:
            raise Exception
        s = s + str(chr(i))
    return s




# do some initialization magic
s = serial.Serial("/dev/ttyUSB0", 57600, timeout=4)
print("sending start...")
s.write(ints2str([128]))
print("switch to full mode...")
s.write(ints2str([132]))

while True:  
    key = getkey()
    if key == keys.UP:
        s.write(ints2str(StraightList))
    elif key == keys.LEFT:
        s.write(ints2str(LeftList))
    elif key == keys.RIGHT:
        s.write(ints2str(RighttList))
    elif key == 'q':
        break 
    time.sleep(0.5)


         
