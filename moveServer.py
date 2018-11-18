import serial
import time
from getkey import getkey, keys
import socket

# this is the port you're connecting to the irobot with
# on windows, this is something like COM2
N = 2

OPCODE_DRIVE = 137
VELOCITY_SECOND = 90
VELOCITY_FIRST = 0

StraightList = [137, 0, 100, 0x80, 0x0]
StopList = [137, 0, 0, 0x80, 0x0]
RightList = [137, 0, 100, 0xFF, 0xFF]
LeftList = [137, 0, 100, 0x00, 0x01]

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


address = ('0.0.0.0', 31500)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)
while True:
    data, addr = s.recvfrom(1)
    if not data:
        print "client has exist"
        break
    key = data[0]
    if key == "u":
        s.write(ints2str(StraightList))
        time.sleep(0.2)      
    elif key == "l":
        s.write(ints2str(LeftList))
        time.sleep(0.2)
        s.write(ints2str(StopList))
    elif key == "r":
        s.write(ints2str(RightList))
        time.sleep(0.2)
        s.write(ints2str(StopList))
    elif key == "d":
        s.write(ints2str(StopList))
        time.sleep(0.2)
    elif key == 'q':
        break 


s.close()