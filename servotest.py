from  gpiozero import AngularServo
from time import sleep

servo = AngularServo(18, min_pulse_width=0.0006,max_pulse_width = 0.0024)
servo.angle = 0

while True:
    servo.angle = 45
    sleep(2)
    servo.angle = 0
    sleep(2)
    servo.angle = -45
    sleep(2)