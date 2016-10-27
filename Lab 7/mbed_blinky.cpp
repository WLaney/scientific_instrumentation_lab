#include "mbed.h"

Serial pc(USBTX, USBRX); // tx, rx
DigitalOut myled(LED1);

int main() {
    while(1) {
        myled = 1;
        wait(0.2);
        myled = 0;
        wait(0.2);
        pc.printf("Hello World!\n");
    }
}