import serial
import time
from gcode_parser import SerialData

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
gcode = open("test.gcode", "r")

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data


while True:
    for gcode_line in gcode:
        if gcode_line[:1] == "G1":
        #if (gcode_line[0] == "G" and gcode_line[1] == "1"):
            if((gcode_line.find("X") != -1) or (gcode_line.find("Y") != -1)):
                num = SerialData(gcode_line)
    value = write_read(num)
    print(value) # printing the value
    time.sleep(4)