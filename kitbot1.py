import RoboPiLib as RPL
import setup
import time
def cease():
    exit(0)
RPL.digitalWrite(18,1)
RPL.digitalWrite(20,0)
RPL.servowrite(1,0)
RPL.servowrite(0,0)
def stop():
    RPL.servowrite(0,0)
    RPL.servowrite(1,0)
def hard_turn_left():
    rpl.servowrite(0,1500)
def turn_left():
    rpl.servowrite(0,1000)
def turn_right():
    rpl.servowrite(1,1000)
def hard_turn_right():
    rpl.servowrite(1,1500)
if rpl.readDistance(1) < 30:
    turn_left()
    start_time=time.time()
    if time.time - start_time > 3:
        cease()
elif rpl.readDistance(0) < 30:
    turn_right()
    start_time=time.time()
    if time.time - start_time > 3:
        cease()
else:
    turn_left()
    turn_right()
