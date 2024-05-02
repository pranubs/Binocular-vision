import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.OUT) #left motor
GPIO.setup(16, GPIO.OUT) #right motor
GPIO.setup(40, GPIO.OUT) #center motor mg995
p = GPIO.PWM(18,50)
pwm = GPIO.PWM(16, 50)
pwm1 = GPIO.PWM(40, 50)
pwm.start(0)
pwm1.start(0)
p.start(0)
def set_angle(p,angle):
	duty_cycle = (angle / 18) + 2
	p.ChangeDutyCycle(duty_cycle)
	sleep(0.5)
	p.ChangeDutyCycle(0)
	p.stop()

set_angle(pwm,10)
set_angle(p,80)

GPIO.cleanup()
