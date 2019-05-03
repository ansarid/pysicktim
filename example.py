# -*- coding: utf-8 -*-
import os
import struct
import ctypes
import pytim5xx as lidar   #   Import TIM5xx Library

os.system('clear')

lidar.scan()

print("Telegram Length: ", lidar.scan.telegram_len, "\n")

print("Command Type:\t",lidar.scan.cmd_type)
print("Command     :\t",lidar.scan.cmd)
print("Version Num :\t",lidar.scan.version)
print("Device Num  :\t",lidar.scan.device_num)

print("Serial Num  :\t",lidar.scan.serial_num)
print("Device Stat :\t",lidar.scan.device_stat)
print("Telegrm Cnt :\t",lidar.scan.telegram_cnt)
print("Scan Count  :\t",lidar.scan.scan_cnt)

print("\nTime since start (\u03BCs):\t\t",lidar.scan.uptime)
print("Time of transmission (\u03BCs):\t",lidar.scan.trans_time)
print("Digital Inputs Status:\t\t",lidar.scan.input_stat)
print("Digital Outputs Status:\t\t",lidar.scan.output_stat)
print("Layer Angle :\t\t\t",lidar.scan.layer_ang)
print("Scan Frequency (Hz):\t\t",lidar.scan.scan_freq)
print("Measurement Frequency (Hz):\t",lidar.scan.meas_freq)
print("Amount of Encoder Data :\t",lidar.scan.enc_amount)
print("# of valid 16 bit channels :\t",lidar.scan.num_16bit_chan)

if dist_start != None:

    print("\n\tDistance\n")

    print("Scale Factor:\t\t\t", lidar.scan.dist_scale_fact)
    print("Scale Factor Offset:\t\t",lidar.scan.dist_scale_fact_offset)
    print("Start Angle:\t\t\t",lidar.scan.dist_start_ang)
    print("Size of single angular step:\t",lidar.scan.dist_angle_res)
    print("Amount of Data:\t\t\t",lidar.scan.dist_data_amnt,"\n")
    print(lidar.scan.distances)

if rssi_start != None:

    print("\n\tRSSI\n")

    print("Scale Factor:\t\t\t", lidar.scan.rssi_scale_fact)
    print("Scale Factor Offset:\t\t",lidar.scan.rssi_scale_fact_offset)
    print("Start Angle:\t\t\t",lidar.scan.rssi_start_ang)
    print("Size of single angular step:\t",lidar.scan.rssi_angle_res)
    print("Amount of Data:\t\t\t",lidar.scan.rssi_data_amnt,"\n")
    print(lidar.scan.rssi)

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
