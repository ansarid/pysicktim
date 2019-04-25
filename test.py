import pysicktim as lidar   #   Import TIM5xx Library

lidar.rstoutpcnt()      # Reset LIDAR before reading.


# data = lidar.eventoutputstate(1)

data = lidar.scandata()    # Tell LIDAR to take reading.
# print()
# print(data)

# lidar.scandata(cont=True,cont_mode=1)    # Tell LIDAR to take readings continuously.

# for x in range(10):
#     data = lidar.read() # Request Reading from LIDAR.
#     print(data)

data = lidar.read() # Request Reading from LIDAR.
# print(data)




print(data)
