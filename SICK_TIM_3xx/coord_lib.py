from math import cos, sin, pi
import numpy as np

def ang2cartezian(axis,distance):
    k = len(distance)
    if(len(axis) == len(distance)):
        pass
    else:
        print "Error: inputs has different lengths"
        print len(axis), len(distance)
        return 0,0
    x = np.zeros(k,np.int16)
    y = np.copy(x)
    for j in range(k):
        x[j] = cos(axis[j]/180.0*pi)*distance[j]
        y[j] = sin(axis[j]/180.0*pi)*distance[j]
    return x,y

def ang_segmentation(scan, max_diff = 150):
    ## Segmentation returns: [start_id, len_of_segment, segment_data]
    segments = []
    segm_start = []
    segm_start.append(0)
    start_segm = 0
    for j in range(len(scan)-1):
        diff = abs(scan[j]-scan[j+1])
        if diff > max_diff:
            if(start_segm == j):
                # throw out single points
                start_segm = j+1
                pass
            else:
                end_segm = j
                segments.append([segm_start[-1],len(scan[start_segm:end_segm+1]),np.asarray(scan[start_segm:end_segm+1])])
                segm_start.append(j+1)
                start_segm = j+1
    segments.append([start_segm,len(scan[start_segm:-1]),np.asarray(scan[start_segm:-1])])
    return segments
