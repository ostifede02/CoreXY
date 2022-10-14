#include "Data_parser.h"
#include <string.h>
#include <stdlib.h>

bool CheckSum(int X_value, int Y_value, int sum_value, int xor_value){
    int sum_check, xor_check = 0;
   
    // check checksum values
    sum_check = X_value + Y_value;
    xor_check = X_value ^ Y_value;

    if((sum_value == sum_check) && (xor_value == xor_check)){
        return true;
    }
    else{
        return false;
    }
}

void GetData(char input_str[], int* X_value, int* Y_value, int* g_cmd, int* sum_value, int* xor_value){
    char* char_ptr;
    int data_buffer[5];
    int index_buffer = 0;
    
    char_ptr = strtok (input_str, ";");
    while (char_ptr != NULL)
    {
        data_buffer[index_buffer] = atoi(char_ptr);
        char_ptr = strtok (NULL, ";");

        index_buffer += 1;
    }

    *X_value = data_buffer[0];
    *Y_value = data_buffer[1];
    *g_cmd = data_buffer[2];
    *sum_value = data_buffer[3];
    *xor_value = data_buffer[4];

    return;
}