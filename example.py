# -*- coding: utf-8 -*-

import os
import struct
import ctypes
import pytim5xx as lidar   #   Import TIM5xx Library





# reset = lidar.rstoutpcnt()      # Reset LIDAR
# print(reset)

# data = lidar.eventoutputstate(1)

# data = lidar.scan()
# print(data)





def uint32(i):
    i = struct.unpack('>i', bytes.fromhex(i))[0]
    return i

os.system('clear')

# data = lidar.scan(raw=True)
data = lidar.demo_data(1)
# data = lidar.demo_data(2)

# data = data.split()
# print(data)

# cmd_type = data[0]
# cmd = data[1]
# v_num = data[2]

dist_start = None
rssi_start = None

for index, item in enumerate(data):
    if "DIST" in item and dist_start == None:
        dist_start = index

    if "RSSI" in item:
        rssi_start = index

# print(dist_start)
# print(rssi_start)

# print(data)

print("\nTelegram Length: ", len(data), "\n")

print("Command Type:\t",data[0])
print("Command     :\t",data[1])
print("Version Num :\t",int(data[2],16))
print("Device Num  :\t",int(data[3],16))
print("Serial Num  :\t",int(data[4],32))
print("Device Stat :\t",int(data[6],8))
print("Telegrm Cnt :\t",int(data[7],16))
print("Scan Count  :\t",int(data[8],16))
print()
print("Time since start (\u03BCs):\t\t",int(data[9],32))
print("Time of transmission (\u03BCs):\t",int(data[10],32))
print("Digital Inputs Status:\t\t",int(data[12],8))
print("Digital Outputs Status:\t\t",int(data[14],8))
print("Layer Angle :\t\t\t",int(data[15],16))
print("Scan Frequency (Hz):\t\t",int(data[16],16)/100)
print("Measurement Frequency (Hz):\t",int(data[17],16)/100) #Math may not be right
print("Amount of Encoder Data :\t",int(data[18],16))
print("# of valid 16 bit channels :\t",int(data[19],16))

if dist_start != None:

    print("\n\tDistance\n")
    #print(data[20])

    print("Scale Factor:\t\t\t",int(data[dist_start+1],16))
    print("Scale Factor Offset:\t\t",int(data[dist_start+2],16))
    print("Start Angle:\t\t\t",uint32(data[dist_start+3])/10000,"°")
    print("Size of single angular step:\t",int(data[dist_start+4],16)/10000,"°")
    data_amnt = int(data[dist_start+5],16)
    print("Amount of Data:\t\t\t",data_amnt,"\n")

    # distances = lidar.scan()
    # print(distances)
    # print(data[26:26+data_amnt])

    dist_end = (dist_start+6) + data_amnt

    # print(dist_start)
    # print(dist_start)
    # print(dist_end)

    distances = lidar.hex_to_meters(data[dist_start+6:dist_end])
    print(distances)

    # print()
    # print(dist_end)
    # print(data[dist_end:len(data)])

if rssi_start != None:

    print("\n\tRSSI\n")

    print("Scale Factor:\t\t\t",data[rssi_start+1])
    print("Scale Factor Offset:\t\t",data[rssi_start+2])
    print("Start Angle:\t\t\t",uint32(data[rssi_start+3])/10000,"°")
    print("Size of single angular step:\t",int(data[rssi_start+4],16)/10000,"°")
    rssi_amnt = int(data[rssi_start+5],16)
    print("Amount of Data:\t\t\t",data_amnt,"\n")

    rssi_end = (rssi_start+6) + rssi_amnt

    rssi = lidar.hex_to_dec(data[rssi_start+6:rssi_end])
    rssi = data[rssi_start+6:rssi_end]
    print(rssi)





# for x in range(10):
#     data = lidar.scan() # Request Reading from LIDAR.
#     print(data)

# firmware = lidar.firmwarev()
# print(firmware)

# ident = lidar.deviceident()
# print(ident)

# name = lidar.readLocationName()
# print(name)

# scan_conf = lidar.scancfg()
# print("\nScan Freq:   ",scan_conf[0],\
#     "\nSectors:     ",scan_conf[1],\
#     "\nAngular Res: ",scan_conf[2],\
#     "\nStart Angle: ",scan_conf[3],\
#     "\nStop Angle:  ",scan_conf[4])

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

# name = lidar.setLocationName("SCUTTLE-Dev")
# print(name)

# factory_def = lidar.loadfacdef()
# print(factory_def)

# passwd = lidar.checkpassword(03,"F4724744")
# print(passwd)

# reboot_status = lidar.reboot()    # Requires Auth
# print(reboot_status)

# config = lidar.scandatacfg()
# print(config)
