def SerialData(gcode_line):
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

    bit_xor = X_value ^ Y_value
    sum = X_value + Y_value
    return [X_value, Y_value, sum, bit_xor]