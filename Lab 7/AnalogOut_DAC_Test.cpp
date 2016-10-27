#include "mbed.h"
 
Serial pc(USBTX, USBRX);
 
// Initialize a pins to perform analog and digital output functions
AnalogOut aout(p18);
char text[128];
float voltage;
 
 
int main(void){
   while (1) {
        pc.printf("Please enter an output voltage\n\r");
        pc.scanf("%s", text);
        voltage = atof(text);
        //pc.printf("Voltage is %f\n\r", voltage);
        // set the output value to be voltage/3.3
        aout = voltage/3.3;
    }
}