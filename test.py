import pysicktim as lidar   #   Import TIM5xx Library

lidar.rstoutpcnt()      # Reset LIDAR before reading.

lidar.scandata(cont=True,cont_mode=1)    # Tell LIDAR to take reading.

for x in range(10):
    data = lidar.read() # Request Reading from LIDAR.
    print(data)
