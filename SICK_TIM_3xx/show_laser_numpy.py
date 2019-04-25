# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import math


## Preparation of variables

base_src = "measurements/Measurement_"
max_dif = 150
number_of_files = 5

ang_values = np.zeros((number_of_files,271),np.int16)
x_values = np.zeros((number_of_files,271),np.float)
y_values = np.zeros((number_of_files,271),np.float)
val_diff = np.zeros((number_of_files-1,271),np.int16)
axis_x = np.arange(-135,136,1,np.float)


## Loading data:

for i in range(number_of_files):
    name = base_src + str(i)
    files = open(name,"r")
    str_data = files.readline().replace(" ","").replace("[","").replace("]","").split(",")
    for j in range(len(str_data)):
        ang_values[i][j] = int(str_data[j])
    files.close()


## Multi segmentation:

segments = []
segm_len = []
segm_start = []

for i in range(number_of_files):
    segments.append([])
    segm_len.append([])
    segm_start.append([0])
    start_segm = 0
    for j in range(270):
        diff = abs(ang_values[i][j]-ang_values[i][j+1])
        if diff > max_dif:
            end_segm = j
            segments[i].append(ang_values[i][start_segm:end_segm+1])
            segm_start[i].append(j)
            segm_len[i].append(len(ang_values[i][start_segm:end_segm+1]))
            start_segm = j+1

    segments[i].append(ang_values[i][start_segm:-1])
    segm_start[i].append(start_segm)
    segm_len[i].append(len(ang_values[i][start_segm:-1]))

npdata = np.asarray(segments)


## Conversion to cartesian:

for i in range(number_of_files):
    for j in range(271):
        x_values[i][j] = math.cos(axis_x[j]/180.0*math.pi)*ang_values[i][j]
        y_values[i][j] = math.sin(axis_x[j]/180.0*math.pi)*ang_values[i][j]


## Show data in polar:

plt.figure(0)
for i in range(number_of_files):
    for j in range(len(segm_start[i])-1):
        if(segm_len[i][j] > 1):
            plt.plot(axis_x[segm_start[i][j]:segm_start[i][j]+segm_len[i][j]],segments[i][j])
        else:
            plt.plot(axis_x[segm_start[i][j]:segm_start[i][j]+segm_len[i][j]],segments[i][j],"*")


## Show data in cartesian:

plt.figure(1)
for i in range(number_of_files):
    for j in range(len(segm_start[i])-1):
        if(segm_len[i][j] > 1):
            plt.plot(x_values[i,segm_start[i][j]+1:segm_start[i][j]+segm_len[i][j]+1],y_values[i,segm_start[i][j]+1:segm_start[i][j]+segm_len[i][j]+1])
        else:
            plt.plot(x_values[i,segm_start[i][j]+1:segm_start[i][j]+segm_len[i][j]+1],y_values[i,segm_start[i][j]+1:segm_start[i][j]+segm_len[i][j]+1],"*")
plt.show()

