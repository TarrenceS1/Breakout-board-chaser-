# Code Foward,Backward,Left, and Right 
import time
import board
import digitalio
import pwmio

from adafruit_motor import motor

PWM_MLA = board.GP12
PWM_MLB = board.GP13

pwm_La = pwmio.PWMOut(PWM_MLA, frequency=100)
pwm_Lb = pwmio.PWMOut(PWM_MLB, frequency=100)

# Runtime Error on line 23 is caused by using wrong
# case for pwm_XX variables on the following line
#Left_Motor = motor.DCMotor(PWM_MLA, PWM_MLB)

def forward()
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1 
	Right_Motor.throttle = Right_Motor_speed
    time.sleep(2) #careful about including time in these. 

def backward()
    Left_Motor_speed = -1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1 
	Right_Motor.throttle = Right_Motor_speed
    time.sleep(2)
    
def left()
    Left_Motor_speed = 0
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = 1 
	Right_Motor.throttle = Right_Motor_speed
    time.sleep
 
def right()
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed
    Right_Motor_speed = -1 
	Right_Motor.throttle = Right_Motor_speed
    time.sleep


while True:
    
    forward()
    backward()
    left()
    right()
    
