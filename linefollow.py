import RPi.GPIO as gpio

# set pin mapping to BOARD
gpio.setmode(gpio.BOARD)


# turn off channel warnings messages
gpio.setwarnings(False)

# Set GPIO pins as output
in1=4
in2=27
in3=22
in4=25
gpio.setup(in1,gpio.OUT)
gpio.setup(in2,gpio.OUT)
gpio.setup(in3,gpio.OUT)
gpio.setup(in4,gpio.OUT)

#gpio.setup(in1,gpio.OUT)#13
#gpio.setup(22,gpio.OUT)#15


# set GPIO pins as inputs
leftSensor = 23
rightSensor = 24

gpio.setup(leftSensor,gpio.IN)
gpio.setup(rightSensor,gpio.IN)

# turn on left motor
def leftOn():
    gpio.output(in1,1)
    gpio.output(in2,0)
    gpio.output(in3,0)
    gpio.output(in4,0)

# turn off left motor
def leftOff():
    gpio.output(in1,0)
    gpio.output(in2,0)
    gpio.output(in3,0)
    gpio.output(in4,0)
    
    
# turn on right motor
def rightOn():
    gpio.output(in1,0)
    gpio.output(in2,0)
    gpio.output(in3,1)
    gpio.output(in4,0)


#turn off right motor
def rightOff():
    gpio.output(in1,0)
    gpio.output(in2,0)
    gpio.output(in3,0)
    gpio.output(in4,0)


# turn off all motors
def stopAll():
    gpio.output(in1,0)
    gpio.output(in2,0)
    gpio.output(in3,0)
    gpio.output(in4,0)


# main program loop

stopAll()   # make sure all pin are set to off

while True:
    
    # if left and right sensors are off stop both motors
    if gpio.input(leftSensor)==0 and gpio.input(rightSensor) == 0:  
        leftOff()
        rightOff()
        
    # if both sensors are on then turn both motors on
    if gpio.input(leftSensor)==1 and gpio.input(rightSensor)==1:
        leftOn()
        rightOn()
        
    # if left sensor is on turn right motor off (pivot left)
    if gpio.input(leftSensor)==1 and gpio.input(rightSensor)==0:
        leftOn()
        rightOff()
        
    # if right sensor is on turn left motor off (pivot right)
    if gpio.input(leftSensor)==0 and gpio.input(rightSensor)==1:
        leftOff()
        rightOn() 
        
gpio.cleanup()
