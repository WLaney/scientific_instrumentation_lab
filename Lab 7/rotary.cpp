#include "mbed.h"

InterruptIn left(p22);
InterruptIn right(p21);
Serial pc(USBTX, USBRX);

int num = 0;
int count = 0;

void ISR_right() {
    if (num==0) num = 1;
    }
    
void ISR_left() {
    if (num==0) num = 2;
    }


int main() {
    left.mode(PullUp);
    right.mode(PullUp);
    right.fall(&ISR_right);
    left.fall(&ISR_left);
    while (1) {
        if (num==1) {
            count += 1;
            pc.printf("%i\n\r", count);
            //pc.printf("num=1\n\r");
            wait(0.1);
            num=0;
        }
        else if (num==2) {
            count -= 1;
            pc.printf("%i\n\r", count);
           // pc.printf("num=2\n\r");
            wait(0.1);
            num=0;
        }
        
        else {}
        
    }
}