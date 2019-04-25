## File for testing on logged data

import matplotlib.pyplot as plt
import numpy as np
import math
from coord_lib import *

base_src = "measurements1/measurement"
max_dif = 150
number_of_files = 1

ang_values = np.zeros(271,np.int16)
axis_x = np.arange(-135,136,1,np.float)

first_run = True

for i in range(number_of_files):
    name = base_src + str(18)
    files = open(name,"r")
    str_data = files.readline().replace(" ","").replace("[","").replace("]","").split(",")
    for j in range(len(str_data)):
        ang_values[j] = int(str_data[j])
    files.close()

    [x,y] = ang2cartezian(axis_x,ang_values)

    ## shift previous data to old ones:
    if(not first_run):
        try:
            del old_angle, old_x, old_y, old_segments, old_segm_len, old_segm_start
            del old_np_data
        except:
            pass
        old_angle = new_angle
        old_x = new_x
        old_y = new_y
        old_segments = new_segments
        try:
            del new_angle, new_x, new_y, new_segments, new_segm_len, new_segm_start
            del new_np_data
        except:
            pass
    else:
        first_run = False

    new_angle = np.asarray(ang_values).astype(np.int16)
    [new_x,new_y]=ang2cartezian(axis_x,new_angle)
    
    ## Segmentation:
    new_segments = ang_segmentation(ang_values, max_diff = 200)

    ## convert segments to cartezian:
    new_x = []
    new_y = []
    for j in range(len(new_segments)):
        [nx,ny] = ang2cartezian(axis_x[new_segments[j][0]:new_segments[j][0]+new_segments[j][1]],new_segments[j][2])
        new_x.append(nx)
        new_y.append(ny)
    
    ## TODO: script for finding human legs near [0,3500] +-[500,500]
    
    ## Show data:
    plt.figure(i)
    #Angular data:
    for j in range(len(new_segments)):
        if(new_segments[j][1] > 1):
            plt.plot(axis_x[new_segments[j][0]:new_segments[j][0]+new_segments[j][1]],new_segments[j][2])
        else:
            plt.plot(axis_x[new_segments[j][0]:new_segments[j][0]+new_segments[j][1]],new_segments[j][2],"*")
    # Cartezian data:
    plt.figure(i+number_of_files)
    for j in range(len(new_segments)):
        plt.plot(new_x[j],new_y[j])
plt.show()
    




