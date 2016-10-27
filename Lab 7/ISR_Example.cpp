//
//  
//  For LPC1768-mbed
//  Uses all five PWM outputs at several steps
//
#include "mbed.h"
//Serial pc(USBTX, USBRX); 

// mbed NXP LPC1768: Any of the numbered mbed pins can be used as an InterruptIn, except p19 and p20.
InterruptIn triggerOut(p26);

//  The DigitalOut Interface can be used on any pin with a blue label, and also with the on-board LEDs (LED1-LED4)
DigitalOut outPulse(p27);

// PWM outputs are pins 22-26  
PwmOut PWM0(p21);  //pin 21 has clock synch
PwmOut PWM1(p26);  //PWM1 output
//PwmOut PWM2(p25);
//PwmOut PWM3(p24);
//PwmOut PWM4(p23);
//PwmOut PWM5(p22);

void flipOut() {
    outPulse = 1;
    outPulse = 0;
    
//    for (int i = 0; i < 200;  i++) {
//    }
    
    outPulse = 1;
    outPulse = 0;
}


// Set Clock Freq with div.
// if mbed is running at 96MHz, div is set 96 to Get 1MHz.
void PWM_SETCLK(int clockCt)
{
    LPC_PWM1->TCR = (1 << 1);               // 1)Reset counter, disable PWM
    LPC_SC->PCLKSEL0 &= ~(0x3 << 12);  
    LPC_SC->PCLKSEL0 |= (4 << 12);          // 2)Set peripheral clock divider to /4, i.e. system clock
    LPC_PWM1->MR0 = clockCt - 1;                // 3)Match Register 0 is shared period counter for all PWM
    LPC_PWM1->MR1 = int(100);            // PWM1 goes low on 100
//    LPC_PWM1->MR2 = int(200);        // PWM2 goes low on 200    
//    LPC_PWM1->MR3 = int(300);         // PWM3 goes low on 300
//    LPC_PWM1->MR4 = int(400);         // PWM4 goes low on 400
//    LPC_PWM1->MR5 = int(500);         // PWM5 goes low on 500
    LPC_PWM1->LER |= 1;                     // 4)Start updating at next period start
//    LPC_PWM1->TCR = (1 << 0) || (1 << 3);   // 5)Enable counter and PWM    
}
int clkCt;
char text[128];
int main() {
    outPulse = 0;  // reset pulse output
// attach and start interrupt
     triggerOut.fall(&flipOut);  // attach the address of the function to the falling edge
   while(1){
//     pc.printf("Please enter an integer clock divider\n\r");
//     pc.scanf("%s", text);
//     clkCt = atoi(text);
     clkCt = 1000;

     PWM_SETCLK(clkCt) ; // Output mbed's "PWM6" pin to 96MHZ/19 = 5.052MHz (Approx)
// Begin process
     LPC_PWM1->TCR = (1 << 0) || (1 << 3);   // Enable counter and PWM    
     wait(5.0); // run for 5 seconds minimum
// End process
//     LPC_PWM1->TCR = (1 << 1);               // Reset counter, disable PWM 
   }
}
