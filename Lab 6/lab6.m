vcc=4.75;
%scope seems to have an offset of -26mv
input=[4095;3583;3071;2559;2047;1535;1023;767;511;255;0];
dc_output=[4.73000000000000;4.15000000000000;3.56000000000000;
    2.94000000000000;2.36000000000000;1.76000000000000;1.19000000000000;
    .877;0.562000000000000;.262;-0.0190000000000000];
dc_output=dc_output+.026;
%plot raw input versue output
figure(1)
plot(input,dc_output,'*')

%convert input to voltage
dcout_expected=(4.75.*input)./(4096);

%percent error, and plot
figure(2)
perror=abs(dc_output-dcout_expected)./dcout_expected;
plot(dcout_expected, perror, '*')
xlabel('expected voltage output')
ylabel('perecent error')
title('percent error vs. expected output')

%function generator gain and lose near 30hz with input sw at 4
%max frequency is 16, 95hz (pluse or minus 2hz)