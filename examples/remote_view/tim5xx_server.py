import socket
import pysicktim as lidar

port = 9999

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(("", port))

while 1:
    try:
        request, ip = socket.recvfrom(1024)
        lidar.scan()
        packet = str(int(lidar.scan.dist_start_ang)) , str(int(lidar.scan.dist_angle_res*10000)) , str(lidar.scan.dist_data_amnt), lidar.scan.raw_distances
        packet = " ".join(packet)
        socket.sendto(packet.encode(), ip)
    except KeyboardInterrupt:
        socket.sendto(packet.encode(), ip)
        pass
