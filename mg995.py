import RPi.GPIO as GPIO
from time import sleep
import socket

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
	#duty_cycle = 
	#GPIO.output(40,True)
	p.ChangeDutyCycle(duty_cycle)
	sleep(0.5)
	#GPIO.output(40,False)
	p.ChangeDutyCycle(0)
	p.stop()
data = "not done"
# Define the IP address and port to listen on
HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 12345      # Choose any available port
angle = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT)) # Bind the socket to the address and port
	    
while(data!="done"):

	# Start listening for incoming connections
	s.listen(5)
	print("Server listening on port", PORT)

	# Accept a connection
	connection, address = s.accept()
	print("Connected to:", address)

	# Receive data from the client
	data = connection.recv(1024).decode()
	print("Received:", data)

	if(data == '+'):
		angle = angle+5
		#set_angle(p,80)
		set_angle(p,angle)
		#set_angle(pwm1,0)
		print("angle=",angle)
	elif(data == '-'):
		angle = angle-5
		set_angle(p,angle)
		#set_angle(pwm1,0)
		print("angle=",angle)
print("done")
GPIO.cleanup()
s.close()
