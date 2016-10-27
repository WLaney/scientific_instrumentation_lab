#include "mbed.h"
 
Serial pc(USBTX, USBRX);
 
// Initialize a pins to perform analog and digital output functions
AnalogOut aout(p18);
char text[128];
float voltage;
char rtext[128];
int i;
float f;

int main(void){
   while (1) {
        pc.printf("Please enter an input\n\r");
        pc.scanf("%s", text);
        //pc.printf("%s\n\r", text);
        i = atoi(text)+5;
        f = atof(text) + 0.1; 
        pc.printf("Your int number plus 5 is %i\n\r", i);
        pc.printf("Your float number plus 0.1 is %f\n\r", f);
        
        //pc.printf("%s\n\r", rtext);
    }
}
