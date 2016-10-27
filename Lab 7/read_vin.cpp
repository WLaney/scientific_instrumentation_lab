#include "mbed.h"

AnalogIn ain(p20); 
Serial pc(USBTX, USBRX);

int main() {
    while(1) {
        float f=ain.read()*3.3;
        pc.printf("Your voltage is %f\n\r", f);
        wait(5);
    }
}