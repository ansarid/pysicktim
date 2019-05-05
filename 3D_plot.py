import pptk
import numpy as np

# LIDAR 85cm Travel on Z-Axis

import math
import numpy as np
import unicodedata

points = 811        # Points per layer
min_angle = -45
angle_res = 0.3333
max_angle = (angle_res * points) + min_angle
layers = 430
list_len = points * layers  # So I know how long to make my array
print(list_len)

x = [0] * list_len
y = [0] * list_len
z = [0] * list_len

crane_height = 0.9144   # meters

data = open("./3D_Data/3D_TEST_3.dat",'r')
data = data.read()

# Yeah I know this is bad but it was 4 A.M.
theta = open("./3D_Data/theta.dat",'r')
theta = theta.read()
theta = theta.replace(" ","")
theta = theta.split(',')
theta = [ float(a) for a in theta ]

data = data.replace("] ! [",",")
data = data.replace("[","")
data = data.replace("]","")
data = data.replace(" ","")
data = data.split(',')
data = [ float(b) for b in data ]

# Convert Polar to Rectangular

for i in range(len(data)-1):
    x[i] = data[i]*math.cos(theta[i])

for i in range(len(data)-1):
    y[i] = data[i]*math.sin(theta[i])

z = np.linspace(0, 0.85, num=list_len)

plot_points = []

for q in range(list_len):
    point = x[q],y[q],z[q]
    plot_points.append(point)

v = pptk.viewer(plot_points)
v.set(point_size=0.001)
