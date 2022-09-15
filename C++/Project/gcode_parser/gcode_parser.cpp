// reading a text file
#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;


void Get_X(char line[], double* X_value);
void Get_Y(char line[], double* Y_value);
bool Is_G1(char line[]);

int main () {
string string_line;
char line[100];
double X_value_string = 0;
double Y_value = 0;
double coordinates[2];
coordinates[0] = coordinates[1] = 0;

ifstream myfile ("example.gcode");
if (myfile.is_open())
{
    while ( getline (myfile, string_line) )
    {
        strcpy(line, string_line.c_str());
        if(Is_G1(line)){
            Get_X(line, &coordinates[0]);
            Get_Y(line, &coordinates[1]);
        }
        else{
            continue;
        }  
        cout << "X: " << coordinates[0] << " Y: " << coordinates[1] << endl;
    }
    myfile.close();
}

else cout << "Unable to open file"; 

return 0;
}

void Get_X(char line[], double* X_value){
    char X_value_string[10];
    int space_index;
    int value_index = 0;

    for(int X_index=0; X_index<strlen(line); ++X_index){
        if(line[X_index] == 'X'){
            space_index = X_index + 1;
            while(line[space_index] != ' '){
                X_value_string[value_index] = line[space_index];
                value_index ++;
                space_index ++;
            }
            X_value_string[value_index] = '\0';

            *X_value = atof(X_value_string);
            // cout << "X: " << X_value << " ";
            break;
        }
    }

    return;
}

void Get_Y(char line[], double* Y_value){
    char Y_value_string[10];
    int space_index;
    int value_index = 0;

    for(int Y_index=2; Y_index<strlen(line); ++Y_index){
        if(line[Y_index] == 'Y'){
            space_index = Y_index + 1;
            while(line[space_index] != ' '){
                Y_value_string[value_index] = line[space_index];
                value_index ++;
                space_index ++;
            }
            Y_value_string[value_index] = '\0';
            *Y_value = atof(Y_value_string);
            // cout << "Y: " << Y_value << "\n";
            break;
        }
    }
    return;
}


bool Is_G1(char line[]){
    if(line[0] == 'G' && line[1] == '1'){
        return true;
    }
    return false;
}
