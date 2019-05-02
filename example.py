import pytim5xx as lidar   #   Import TIM5xx Library

# reset = lidar.rstoutpcnt()      # Reset LIDAR
# print(reset)

# data = lidar.eventoutputstate(1)

# for x in range(10):
#     data = lidar.scandata() # Request Reading from LIDAR.
#     print(data)

# firmware = lidar.firmwarev()

# print(firmware)
# ident = lidar.deviceident()
# print('\n'+ident)

# name = lidar.setLocationName("SCUTTLE-Dev")
# print(name)

# name = lidar.readLocationName()
# print(name)

# scan_conf = lidar.scancfg()
# print("\nScan Freq:   ",scan_conf[0],\
#     "\nSectors:     ",scan_conf[1],\
#     "\nAngular Res: ",scan_conf[2],\
#     "\nStart Angle: ",scan_conf[3],\
#     "\nStop Angle:  ",scan_conf[4])

# data = lidar.scan(raw=True)    # Tell LIDAR to take reading.
# print()
# print(data)

# data = lidar.scan()    # Tell LIDAR to take reading.
# print()
# print(data)

# maint = lidar.setaccessmode(user="02", password="B21ACE26")
# print(maint)

# auth = lidar.setaccessmode(user="03", password="F4724744")
# print(auth)

# serv = lidar.setaccessmode(user="04", password="81BE23AA")
# print(serv)

# start = lidar.startmeas()
# print(start)

# stop = lidar.stopmeas()
# print(stop)

# factory_def = lidar.loadfacdef()
# print(factory_def)

# passwd = lidar.checkpassword(03,"F4724744")
# print(passwd)

# reboot_status = lidar.reboot()    # Requires Auth
# print(reboot_status)

# config = lidar.scandatacfg()
# print(config)
