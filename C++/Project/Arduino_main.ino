#include "Data_parser.h"
#include "CoreXY_class.h"

CoreXY coreOBJ(400, 11000, 10);

void setup()
{
    pinMode(LX_Stepper_DIR, OUTPUT);
    pinMode(LX_Stepper_STEPS, OUTPUT);
    pinMode(RX_Stepper_DIR, OUTPUT);
    pinMode(RX_Stepper_STEPS, OUTPUT);

    pinMode(LED_BUILTIN, OUTPUT);

    Serial.begin(9600);
    Serial.setTimeout(200);
}

void loop() 
{
    const int data_size = 30;
    char data_input[data_size] = {'\0'};
    String string_data_input;
    int X_value, Y_value, g_cmd, sum_value, xor_value = 0;
    float flt_X_value, flt_Y_value = 0;
    
    // from string to char array
    string_data_input = Serial.readStringUntil('\0');
    strcpy(data_input, string_data_input.c_str());

    GetData(data_input, &X_value, &Y_value, &g_cmd, &sum_value, &xor_value);

    flt_X_value = X_value/10;
    flt_Y_value = Y_value/10;

    if(CheckSum(X_value, Y_value, sum_value, xor_value)){
        // push-pull pen
        // coreOBJ.g_command(g_cmd);
        // execute coordinates
        coreOBJ.GoTo_Relative(flt_X_value, flt_Y_value);
        // send ACK message
        Serial.print("ACK");
    }
    else{
        // send NAK message!
        Serial.print("NAK");
    }
    Serial.flush();
}