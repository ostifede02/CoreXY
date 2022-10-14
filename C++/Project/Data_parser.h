#ifndef DATA_PARSER
#define DATA_PARSER

void GetData(char input_str[], int* X_value, int* Y_value, int* g_cmd, int* sum_value, int* xor_value);
bool CheckSum(int X_value, int Y_value, int sum_value, int xor_value);

#endif
