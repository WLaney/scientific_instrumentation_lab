//
//  
//  For LPC1768-mbed
//  Uses all six PWM outputs at several steps
//
 
#include "mbed.h"
 
PwmOut fmclck(p21);     // PWM1[6]
PwmOut PWM2(p22);
PwmOut PWM3(p23);
PwmOut PWM4(p24);
PwmOut PWM5(p25);
Serial pc(USBTX, USBRX);
 
// Set Clock Freq with div.
// if mbed is running at 96MHz, div is set 96 to Get 1MHz.
void PWM6_SETCLK(int div)
{
    LPC_PWM1->TCR = (1 << 1);               // 1)Reset counter, disable PWM
    LPC_SC->PCLKSEL0 &= ~(0x3 << 12);  
    LPC_SC->PCLKSEL0 |= (1 << 12);          // 2)Set peripheral clock divider to /1, i.e. system clock
    LPC_PWM1->MR0 = div - 1;                // 3)Match Register 0 is shared period counter for all PWM
    LPC_PWM1->MR1 = 20;                      // PWM1 goes low on 5
    LPC_PWM1->MR2 = 30;                      // PWM2 goes low on 1    
    LPC_PWM1->MR3 = 40;                      // PWM3 goes low on 9
    LPC_PWM1->MR4 = 50;                      // PWM4 goes low on 11
    LPC_PWM1->MR5 = 60;                      // PWM5 goes low on 13
    LPC_PWM1->LER |= 1;                     // 4)Start updating at next period start
    LPC_PWM1->TCR = (1 << 0) || (1 << 3);   // 5)Enable counter and PWM    
}
 
int main() {   
    pc.printf("starting");     
    PWM6_SETCLK(100) ; // Output mbed's "PWM6" pin to 96MHZ/19 = 5.052MHz (Approx)
    while(1){
        wait(1.0); // Gate time for count
    }
}