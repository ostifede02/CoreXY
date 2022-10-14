#include "CoreXY_class.h"
#include "math.h"
#include "Arduino.h"

CoreXY::CoreXY(int steps_per_revolution_input, int speed_mmMin_input, double steps_per_mm_input){
    steps_per_revolution = steps_per_revolution_input;
    speed_mmMin = speed_mmMin_input;
    steps_per_mm = steps_per_mm_input;
    myPosition.x = myPosition.y = 0;
    return;
}

void CoreXY::GoTo_Absolute(double inputX, double inputY){
    double newX, newY = 0;
    newX = inputX - myPosition.x;
    newY = inputY - myPosition.y;

    Coordinates2Stepper(newX, newY);

    myPosition.x = newX; 
    myPosition.y = newY;
    return;
}

void CoreXY::GoTo_Relative(double inputX, double inputY){

    Coordinates2Stepper(inputX, inputY);
    
    myPosition.x += inputX; 
    myPosition.y += inputY;
    return;
}

void CoreXY::GoTo_Home(void){

    Coordinates2Stepper(-myPosition.x, -myPosition.y);
    
    myPosition.x = 0; 
    myPosition.y = 0;
    return;
}

void CoreXY::Coordinates2Stepper(double inputX, double inputY){
    int L_steps, R_steps = 0;
    double L_travel_in_mm, R_travel_in_mm = 0;
    double distance_in_mm = 0;
    long int time_in_micros = 0;

    distance_in_mm = sqrt(pow(inputX,2) + pow(inputY,2));
    time_in_micros = (distance_in_mm*60*1000000) / speed_mmMin;

    // LEFT Stepper
    L_steps = round(Distance2Step(inputX - inputY));
    // RIGHT Stepper
    R_steps = round(Distance2Step(inputX + inputY));

    // StepperMovement(L_steps, R_steps, time_in_micros);
    StepperMovementAcceleration(L_steps, R_steps, time_in_micros);
    return;
}

void CoreXY::StepperMovement(int L_steps, int R_steps, long int time_micros){
  SetDirection(L_steps, R_steps);
  L_steps = abs(L_steps);
  R_steps = abs(R_steps);
 
  long int L_delay = time_micros /((L_steps - 1));
  long int R_delay = time_micros /((R_steps - 1));

  double L_counter = 0;
  double R_counter = 0;

  long int time_dt = 0;
  long int time_start = micros();

 
  while(true){
    time_dt = micros() - time_start;
   
    if ((L_counter < L_steps) && (time_dt >= L_delay*L_counter)){
      OneStepLX();
      L_counter += 1;
    }

    time_dt = micros() - time_start;
   
    if ((R_counter < R_steps) && (time_dt >= R_delay*R_counter)){
      OneStepRX();
      R_counter += 1;
    }

    if ((L_counter >= L_steps) && (R_counter >= R_steps)){
      break;
    }
  }
  return;
}

void CoreXY::StepperMovementAcceleration(int L_steps, int R_steps, long int time_micros){
    SetDirection(L_steps, R_steps);
    L_steps = abs(L_steps);
    R_steps = abs(R_steps);

    float L_bezier_coefficent = 1/(L_steps-1);
    float R_bezier_coefficent = 1/(R_steps-1);

    float L_counter = 0;
    float R_counter = 0;

    float L_bezier_input = 0;
    float R_bezier_input = 0;

    int L_delay = 0;
    int R_delay = 0;

    long int time_dt = 0;
    long int time_start = micros();


    while(true){
        time_dt = micros() - time_start;

        if ((L_counter < L_steps) && (time_dt >= L_delay)){
            OneStepLX();
            L_counter += 1;
            L_bezier_input = L_bezier_coefficent * L_counter;
            L_delay = BezierCurve(L_bezier_input) * time_micros;
        }

        time_dt = micros() - time_start;

        if ((R_counter < R_steps) && (time_dt >= R_delay)){
            OneStepRX();
            R_counter += 1;
            R_bezier_input = R_bezier_coefficent * R_counter;
            R_delay = BezierCurve(R_bezier_input) * time_micros;
        }

        if ((L_counter >= L_steps) && (R_counter >= R_steps)){
            break;
        }
    }
    return;
}

int CoreXY::BezierCurve(float bezier_input){
    Point P0{0, 0};
    Point P1{0, 0.8};
    Point P2{1, 0.2};
    Point P3{1, 1};
    
    float ya, yb, yc;
    float ym, yn;
    float bezier_delay;

    ya = BezierPoint(P0.y, P1.y, bezier_input);
    yb = BezierPoint(P1.y, P2.y, bezier_input);
    yc = BezierPoint(P2.y, P3.y, bezier_input);

    ym = BezierPoint(ya ,yb ,bezier_input);
    yn = BezierPoint(yb ,yc ,bezier_input);

    bezier_delay = BezierPoint(ym, yn, bezier_input);

    return bezier_delay;
}

float CoreXY::BezierPoint(float n1, float n2, float n){
    return (n1+((n2 - n1)*n));
}

void CoreXY::SetDirection(int L_steps, int R_steps){
  // setting the direction
  if(L_steps >= 0){
      digitalWrite(LX_Stepper_DIR, HIGH);
  }
  else{
      digitalWrite(LX_Stepper_DIR, LOW);
  }
  if(R_steps >= 0){
      digitalWrite(RX_Stepper_DIR, HIGH);
  }
  else{
      digitalWrite(RX_Stepper_DIR, LOW);
  }
  
  return;
}

double CoreXY::Distance2Step(double distance){
    return distance * steps_per_mm;
}

void CoreXY::OneStepLX(void){
    digitalWrite(LX_Stepper_STEPS, HIGH);
    delayMicroseconds(80);
    digitalWrite(LX_Stepper_STEPS, LOW);
    return;  
}

void CoreXY::OneStepRX(void){
    digitalWrite(RX_Stepper_STEPS, HIGH);
    delayMicroseconds(80);
    digitalWrite(RX_Stepper_STEPS, LOW);
    return;  
}

void CoreXY::gCommand(int g_cmd){
    if(g_cmd == 0){
        digitalWrite(LINEAR_ACTUATOR_1, HIGH);
    }
    else if(g_cmd == 1){
        digitalWrite(LINEAR_ACTUATOR_1, LOW);
    }
    return;  
}
