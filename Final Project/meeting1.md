# Electronics Final, Meeting 1


Will do fish tank monitoring project


## Project Overview


Group name ideas


- electric fish bowl
- mega electric fishbowl
- __6 billion dollar fish tank (make better faster stronger)__


What to monitor


- PH 
- Salinity
- water temperature
- water height


Will use a Pi to monitor sensors. We do not need frequent sampling and we want easy internet connectivity


What is will do


- read from the sensors
- log the data, log once a minute and day averages
- send out email alerts at extreme points


Stretch goals


- log down time, ie when the system is powered off
- send out text message alerts 
- attached LCD screen for release time data display
- connect colored tank lighting
- controllable via text message
- water proof the pi
- restart sensing on boot
- interface with devices to fix imbalances
- video live stream


## Part list


Ph is to expensive, so we will not do it


[Temp sensor](https://www.adafruit.com/products/381), $9.95


[Water level](https://www.adafruit.com/products/464), $39.95


[Camera](https://www.adafruit.com/products/3099), $29.95


[Light sensor](https://www.adafruit.com/products/439?gclid=CjwKEAjwnebABRCjpvr13dHL8DsSJABB-ILJZXrfROdQyL3M57e0ZX2USmHaqlusaR8f66DtR_TGuxoCp-7w_wcB), $5.95


Salinity is also expensive


Enclosure for Pi will be 3d printed in makerspace


ADC, borrow from electronics lab


## Programing


We want to start by trying to send text messages and emails from the pi while we wait for sensors to come in. Then we will try to get each sensor to write readings to a text file independently with a time stamp. Then get the sensors to read together and write to the text file. (the reading/ writing will be not be truly simultaneous but we don't care, it will be close enough).


Develop code to look for large deviation in data to send alerts. Also create profiles to send alerts when condition would kill a specific fish.


Develop code to respond to an incoming text/email.


Develop code to stream video of the fish tank. We can do this through a web app we found. 


### Dev Plan


1. send text/email from pi
2. respond to incoming text/email
3. set up web streaming
4. get sensors to write to log file independently
5. get sensors to write to same log file
6. send out log file
7. send out alerts from large data changes
8. alert on power resets


## Quality assurance


- Test sensors against data sheet
- Test sensors against other sensor
- Test notification by changing water characteristics
- Make sure we can send and receive data from the Pi
- Run for 24+ hours to check for hidden problems, check data to make sure we do not miss events
- Take multiple measurements in same condition to isolate random error
- Flicker power to test boot conditions
- Blind test, ie have someone screw with thing and see if we can figure out what they did/get notified when it happens
- Try running at different sampling rates to test bounds of system
- Test data reading at same time as video stream
- Test response to text/email inputs while video streaming
- recoded heat of Pi in enclosure doing various task to ensure it will not overheat


## Tasks for next week


Ben: Begin CAD designs of the box for pi


William: Send emails from python


Edward: Send text messages, look into receiving messages


Ian: Setup pi camera
