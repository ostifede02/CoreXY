from gcode_parser import SerialCommunication

gcode = open(r"C:\Users\ostif\Documents\CoreXY\Python\circle_gcode.gcode", "r")

for gcode_line in gcode:
    # gcode_cmd = gcode_line.split(" ")[0]
    gcode_cmd = gcode_line[0:2]
    
    if gcode_cmd == "G0":
        SerialCommunication(gcode_line, "G0")
    elif gcode_cmd == "G1":
        SerialCommunication(gcode_line, "G1")
    elif gcode_cmd == "G28":
        pass