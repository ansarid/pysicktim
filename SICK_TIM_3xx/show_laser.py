import matplotlib.pyplot as plt
import numpy as np
import math

base_src = "measurements/Measurement_"
max_dif = 150

data=[]

for i in range(40):
    name = base_src + str(i)
    files = open(name)
    str_data = files.readline().replace(" ","").replace("[","").replace("]","").split(",")
    int_data = []
    for j in range(len(str_data)):
        int_data.append(int(str_data[j]))
    data.append(int_data)


## SHOW in angles (python array)

x = range(-135,136,1)
for i in range(0):
    plt.figure()
    plt.plot(x,data[i])
    plt.show()

data_index = 1

segments = []
segm_len = []
segm_start = []
start_segm = 0
segm_start.append(0)
for i in range(270):
    diff = abs(data[data_index][i]-data[data_index][i+1])
    if diff > max_dif:
        end_segm = i
        segments.append(data[data_index][start_segm:end_segm+1])
        segm_start.append(i)
        segm_len.append(len(data[data_index][start_segm:end_segm+1]))
        start_segm = i+1

segments.append(data[data_index][start_segm:-1])
segm_start.append(start_segm)
segm_len.append(len(data[data_index][start_segm:-1]))

plt.figure(1)
plt.subplot(221,autoscale_on = False, ylim = (0,4000), xlim = (-135,135))
plt.plot(x,data[data_index])
plt.subplot(223,autoscale_on = False, ylim = (0,4000), xlim = (-135,135))

for i in range(len(segm_len)):
    x_angle = range(segm_start[i]-135,segm_start[i]+segm_len[i]-135)
    if(len(x_angle) > 1):
        plt.plot(x_angle,segments[i])
    else:
        plt.plot(x_angle,segments[i],"*")

## tranform to cartezian
x=[]
y=[]
for i in range(271):
    x.append(math.cos((i-135)/180.0*math.pi)*data[data_index][i])
    y.append(math.sin((i-135)/180.0*math.pi)*data[data_index][i])

plt.subplot(222)
plt.plot(x,y)

del x,y
plt.subplot(224)
for i in range(len(segm_len)):
    x_angle = range(segm_start[i]-135,segm_start[i]+segm_len[i]-135)
    x = []
    y = []
    for j in range(len(x_angle)):
        x.append(math.cos(x_angle[j]/180.0*math.pi)*segments[i][j])
        y.append(math.sin(x_angle[j]/180.0*math.pi)*segments[i][j])
    if(len(x_angle) > 1):
        plt.plot(x,y)
    else:
        plt.plot(x,y,"*")
    del x,y

plt.show()
