#include "CoreXY_class.h"

CoreXY coreOBJ(400, 11000, 10);

void setup()
{
  pinMode(LX_Stepper_DIR, OUTPUT);
  pinMode(LX_Stepper_STEPS, OUTPUT);
  pinMode(RX_Stepper_DIR, OUTPUT);
  pinMode(RX_Stepper_STEPS, OUTPUT);

  Serial.begin(9600);
}

void loop() 
{
  coreOBJ.GoTo_Relative(200, 200);
  delay(1000);
  coreOBJ.GoTo_Relative(-200, -200);
  delay(1000);
}
