import math
import socket
import pytim5xx as lidar

port = 9999

clients = []
ip = None

packet = []

# set up the socket using local address
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(("", port))

while 1:

    lidar.scan()

    packet = lidar.scan.raw_distances

    request, ip = socket.recvfrom(1024)
    socket.sendto(packet.encode(), ip)
