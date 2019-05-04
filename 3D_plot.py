from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection='3d')

# LIDAR 85cm Travel on Z-Axis

import math
import numpy as np
import unicodedata

i = 0



points = 811
min_angle = -45
angle_res = 0.3333
max_angle = (angle_res * points) + min_angle

layers = 430

x = [0] * 348730
y = [0] * 348730
z = [0] * 348730

# 348730 total data points

crane_height = 0.9144   # meters

data = open("./3D_Data/3D_TEST_1.dat",'r')
data = data.read()

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



# print(len(x))
# print(len(y))
# print(len(z))

print(data[100])
print(theta[100])

print(x[100])
print(y[100])
# print(z[0])


z = np.linspace(0, 0.85, num=layers)

# plt.scatter(x, y, s=0.1, alpha=0.5)
ax.scatter3D(x, y, z, c=z, cmap='Greens');
# ax.scatter3D(theta, data, z, c=z, cmap='Greens');
plt.show()
