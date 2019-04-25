import pysicktim as lidar

lidar.rstoutpcnt()

while 1:
    lidar.scandata()
    data = lidar.read()
    print(data)
