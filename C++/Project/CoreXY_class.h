#ifndef COREXY_H
#define COREXY_H

#define LX_Stepper_DIR 8
#define LX_Stepper_STEPS 9
#define RX_Stepper_DIR 10
#define RX_Stepper_STEPS 11
#define LINEAR_ACTUATOR_1 12

struct Position{
    double x;
    double y;
};

struct Point{
    float x;
    float y;
};


class CoreXY{
    public:
        CoreXY(int steps_per_revolution, int speed_mmMin, double steps_per_mm);
        void GoTo_Absolute(double inputX, double inputY);
        void GoTo_Relative(double inputX, double inputY);
        void GoTo_Home(void);
        void gCommand(int g_cmd);

        //void StepperMovement(int L_steps, int R_steps, long int time_in_micros);
    private:
        int steps_per_revolution;
        int speed_mmMin;
        double steps_per_mm;
        Position myPosition;

        void Coordinates2Stepper(double newX, double newY);
        void StepperMovement(int L_steps, int R_steps, long int time_in_micros);
        void StepperMovementAcceleration(int L_steps, int R_steps, long int time_micros);
        double Distance2Step(double distance);
        void OneStepLX(void);
        void OneStepRX(void);
        void SetDirection(int L_steps, int R_steps);
        int BezierCurve(float bezier_input);
        float BezierPoint(float n1, float n2, float n);
};

#endif