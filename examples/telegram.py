# -*- coding: utf-8 -*-
import os
import pysicktim as lidar   #   Import TIM5xx Library as "lidar"

os.system('clear')

data = lidar.scan()

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

print("\n\tDistance\n")

print("Scale Factor:\t\t\t", lidar.scan.dist_scale_fact)
print("Scale Factor Offset:\t\t",lidar.scan.dist_scale_fact_offset)
print("Start Angle:\t\t\t",lidar.scan.dist_start_ang)
print("Size of single angular step:\t",lidar.scan.dist_angle_res)
print("Amount of Data:\t\t\t",lidar.scan.dist_data_amnt,"\n")
print(lidar.scan.distances)

print("\n\tRSSI\n")

print("Scale Factor:\t\t\t", lidar.scan.rssi_scale_fact)
print("Scale Factor Offset:\t\t",lidar.scan.rssi_scale_fact_offset)
print("Start Angle:\t\t\t",lidar.scan.rssi_start_ang)
print("Size of single angular step:\t",lidar.scan.rssi_angle_res)
print("Amount of Data:\t\t\t",lidar.scan.rssi_data_amnt,"\n")
print(lidar.scan.rssi)
