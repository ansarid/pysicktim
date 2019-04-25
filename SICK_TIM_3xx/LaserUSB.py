#import sys
import time
#from threading import Thread,Event,Lock
import usb.core
import usb.util

import numpy as np
import matplotlib.pyplot as plt
import math
from coord_lib import *

class TIM3xx:
    def __init__(self):
        self.dev = usb.core.find(idVendor=0x19a2, idProduct=0x5001)
        ##self.dev.set_configuration()
        for i in range(10):
            try:
                self.dev.set_configuration()
                print "Connection succesfull"
                break
            except:
                print "Conect error " +str(i)
                time.sleep(0.1)

    def __del__(self):
        del self.dev

    def send_cmd(self, cmd):
        for i in range(10):
            try:
                self.dev.write(2|usb.ENDPOINT_OUT,"\x02"+cmd+"\x03\0",0)
                arr = self.dev.read(1|usb.ENDPOINT_IN,65535,timeout=100)
                return "".join([chr(x) for x in arr[1:-1]])
            except:
                time.sleep(0.001)

    def internal_scan(self):
        data = self.send_cmd('sRN LMDscandata').split()
        if len(data) == 580:
            dist = [int(x,16) for x in data[26:271+26]]
            remission = [int(x,16) for x in data[304:-5]]
            run_time = int(data[9],16);
        else:
            print "Corrupted data, data_len = " + str(len(data))
        return run_time, dist, remission


number_of_measurements = 40

laser = TIM3xx()
datas = []
ang_values = np.zeros((271),np.int16)
axis_x = np.arange(-135,136,1,np.float)

for i in range(number_of_measurements):
    [running, distance, remission] = laser.internal_scan()

    ## Conversion to numpy array:
    for j in range(len(distance)):
        ang_values[j] = int(distance[j])

    ## Segmentation
    segments = ang_segmentation(ang_values, max_diff = 100)

    ## convert segments to cartezian:
    new_x = []
    new_y = []
    for j in range(len(segments)):
        [nx,ny] = ang2cartezian(axis_x[segments[j][0]:segments[j][0]+segments[j][1]],segments[j][2])
        new_x.append(nx)
        new_y.append(ny)

    ## Show data:
    plt.figure(i)
    #Angular data:
    for j in range(len(segments)):
        plt.plot(axis_x[segments[j][0]:segments[j][0]+segments[j][1]],segments[j][2])
    # Cartezian data:
    plt.figure(i+number_of_measurements)
    for j in range(len(segments)):
        plt.plot(new_x[j],new_y[j])
    plt.show()
    
    datas.append(distance)
del laser




