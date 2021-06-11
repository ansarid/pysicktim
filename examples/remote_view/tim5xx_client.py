import math
import socket
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class network:

    ip = "192.168.1.16"
    port = 9999

try:

    socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket.settimeout(0.001)

except socket.error:

    print("Oops, something went wrong connecting the server!")
    exit()

fig = plt.figure()
fig.canvas.set_window_title('TiM5xx LIDAR Monitor')
lidar_polar = plt.subplot(polar=True)

def animate(i):

    try:

        message = "0".encode()
        socket.sendto(message, (network.ip, network.port))
        data, ip = socket.recvfrom(4000)
        data = data.split()

        min_angle = int(data[0])
        angle_res = float(data[1])/10000
        points = int(data[2])
        distances = [int(x,16)/1000.0 for x in data[3:] ]
        max_angle = (angle_res * points) + min_angle
        # max_distance = 10
        max_distance = 6
        min_distance = 0.002

        if max(distances) > max_distance or min(distances) < min_distance:	# Check if any items in list are larger than max_distance

            for i in range(len(distances)):	            # Iterate through list and set any integers larger than max_distance to max_distance

                if distances[i] > max_distance:		    # if larger than max_distance
                    distances[i] = max_distance	        # set equal to max_distance

                if distances[i] <= min_distance:		# if larger than max_distance
                    distances[i] = max_distance	        # set equal to max_distance

        theta = np.linspace(min_angle,max_angle,points)
        theta = (np.pi/180.0 )*theta    # in radians
        theta = [ float(x) for x in theta ]

        lidar_polar.clear()
        lidar_polar.set_thetamin(min_angle)
        lidar_polar.set_thetamax(max_angle)
        plt.fill_between(theta, distances, alpha=0.2)
        lidar_polar.scatter(theta, distances, s=1, c=distances)   # Colored Points

    except:

        pass

ani = animation.FuncAnimation(fig, animate)
plt.show()
