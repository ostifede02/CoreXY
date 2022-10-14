import serial
from gcode_parser import SerializedData


arduino = serial.Serial(port='COM3', baudrate=9600, timeout=0.1)
gcode = open("C:\\Users\\ostif\\Documents\\CoreXY\\Python\\test1.gcode", "r")

def SerialCommunication(g_cmd):
    errorflag = True
    while errorflag:
        check_comm_str = ""

        sent = arduino.write(SerializedData(gcode_line, g_cmd))
        print("Sent ", sent, " bytes")
        
        while check_comm_str == "":
            check_comm_str = arduino.readline().decode("utf-8")

        if(check_comm_str == "ACK"):
            # ACK: Succesfull, go ahed
            print(SerializedData(gcode_line))
            print("Succes")
            errorflag = False
        elif(check_comm_str == "NAK"):
            # NAK: Error occured
            print("Failed")
            errorflag = True
        else:
            print("*******NONE*******")
            pass


for gcode_line in gcode:
    gcode_cmd = gcode_line.split(" ")[0]
    if gcode_cmd == "G0":
        SerialCommunication("G0")
    elif gcode_cmd == "G1":
        SerialCommunication("G1")
    elif gcode_cmd == "G28":
        pass