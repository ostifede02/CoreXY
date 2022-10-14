import serial

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=0.1)

# return the data string to send to arduino
def SerializedData(gcode_line, g_cmd):
    start_index = gcode_line.find("X") + 1
    end_index = gcode_line.find(" ", start_index)
    X_value = round(float(gcode_line[start_index:end_index]), 1)
    X_value *= 10
    X_value = int(X_value)

    start_index = gcode_line.find("Y") + 1
    end_index = gcode_line.find(" ", start_index)
    Y_value = round(float(gcode_line[start_index:end_index]), 1)
    Y_value *= 10
    Y_value = int(Y_value)

    g_cmd = int(g_cmd[1:])

    sum = X_value + Y_value
    bit_xor = X_value ^ Y_value

    return bytes(f"{X_value};{Y_value};{g_cmd};{sum};{bit_xor}\0", "utf-8")


def SerialCommunication(gcode_line, g_cmd):
    errorflag = True
    while errorflag:
        check_comm_str = ""

        sent = arduino.write(SerializedData(gcode_line, g_cmd))
        print("Sent ", sent, " bytes")
        
        while check_comm_str == "":
            check_comm_str = arduino.readline().decode("utf-8")

        if(check_comm_str == "ACK"):
            # ACK: Succesfull, go ahed
            print(SerializedData(gcode_line, g_cmd))
            print("Succes")
            errorflag = False
        elif(check_comm_str == "NAK"):
            # NAK: Error occured
            print("Failed")
            errorflag = True
        else:
            print("*******NONE*******")
            pass