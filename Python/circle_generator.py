import math as m

def DrawCircle(radius, resolution):
    gcode = open("circle_gcode.gcode", "w")

    for t in range(0, resolution+1):
        x_value = round(radius*m.cos((2*m.pi/resolution)*t), 2)
        y_value = round(radius*m.sin((2*m.pi/resolution)*t), 2)
        
        gcode.write(f"{x_value} {y_value}\n")
        # gcode.write(f"G1 X{x_value} Y{y_value}\n")

    gcode.close()
    print("File succesfully created!")
    
DrawCircle(20, 6)