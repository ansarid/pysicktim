# This example moves the servos to the position specified by "duty."
# If the servo is a continuous type, the duty will set the speed instead of the position.

import time
import math
import socket
import numpy as np
import matplotlib
from subprocess import Popen, PIPE
import Adafruit_GPIO.I2C as Adafruit_I2C
import pytim5xx as lidar   #   Import TIM5xx Library

import rcpy
import rcpy.mpu9250 as mpu9250

# defaults
duty = 0	# Duty cycle (-1.5,1.5)
period = 0.02	# Set servo period to 20ms
channel = 0	# Which channel (1-8), 0 outputs to all channels

lidar.rstoutpcnt()      # Reset LIDAR before reading.

rcpy.set_state(rcpy.RUNNING)

mpu9250.initialize(enable_dmp=True,
                   dmp_sample_rate=100,
                   enable_fusion=False,
                   enable_magnetometer=False)

port = 9999

clients = []
ip = None

packet = []

min_angle = -45
max_angle = 225

# angle_res = 0.33
points = 810

telegram_start = 28

max_distance = 2


def read_encoder(enc):
    try:
        x = enc.readU16(0xFE)
        x = ((x << 8) | (x >> 8)) & 0xFFFF
        meas = ((x & 0xFF00) >> 2) | ( x & 0x3F)
        angle = meas*0.0219

    except:
        print('Warning (I2C): Could not read ', enc , "!")
        angle = 0

    return angle

def imu():

    # running
    if rcpy.get_state() == rcpy.RUNNING:

        data = mpu9250.read()
        data = data['tb']        # Get imu Value and Convert to Degrees (0 to 180 , -180 to 0)
#                data = (math.degrees(round(data[2],2)))     # Convert IMU reading to degrees
        data = (math.degrees(round(data[2],2))) % 360     # Convert IMU reading to degrees


    return data



def minimum(a, n):

    # inbuilt function to find the position of minimum
    minpos = a.index(min(a))

    return minpos

theta = np.linspace(min_angle,max_angle,points)
degrees = [ round(float(x),2) for x in theta ]
theta = (np.pi/180.0 )*theta    # in radians
theta = [ float(x) for x in theta ]



# set up the socket using local address
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(("", port))

r_encoder = Adafruit_I2C.Device(0x41,1)
l_encoder  = Adafruit_I2C.Device(0x42,1)

#
# rcpy.set_state(rcpy.RUNNING)
#
# srvo = servo.Servo(channel)	# Create servo object
#
# clck = clock.Clock(srvo, period)	# Set PWM period for servos

try:

    #
    # # enable servos
    # servo.enable()		# Enables 6v rail
    #
    # # start clock
    # clck.start()		# Starts PWM

    # keep running
    while 1:


        data = lidar.scan(raw=True)    # Tell LIDAR to take reading.

        l_wheel = int(read_encoder(l_encoder)*10)
        r_wheel = int(read_encoder(r_encoder)*10)
        imu_angle = int(imu()*10)

        print(data)

        packet = data + "." +str(l_wheel) + "." + str(r_wheel) + "." + str(imu_angle)

        request, ip = socket.recvfrom(1024)
        client_ip = ip[0]

        if client_ip not in clients:

            clients.append(client_ip)



        socket.sendto(packet.encode(), ip)

        data = data.split(' ')
        data = data[telegram_start:telegram_start+points]
        data = [ int(x,16)/1000 for x in data ]

        print(data)

        if max(data) > max_distance:	# Check if any items in list are larger than max_distance

            for i in range(len(data)):	# iterate through list and set any integers larger than max_distance to max_distance

                if data[i] > max_distance:		# if larger than max_distance
                    data[i] = max_distance	# set equal to max_distance

                if data[i] <= 0.002:		# if larger than max_distance
                    data[i] = max_distance	# set equal to max_distance



        data[len(data)-1] = 0.4

        close = minimum(data, len(data))
        # print(close)
        closest_deg = 0

        if data[close] > 0.1:
            closest_deg = degrees[close]

        closest_deg = float((-0.0095238*closest_deg)+1.07142857)

        # print(closest_deg)
        # srvo.set(round(closest_deg,2))	# Set servo duty

except KeyboardInterrupt:

	pass

finally:


	# say bye
	print("\nExiting")
