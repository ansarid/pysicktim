# Import pysicktim library as "lidar"
import pysicktim as lidar

# Repeat code nested in for loop 10 times
for x in range(10):
# while True:

	lidar.scan()	# Requests and returns list of LiDAR
			# distance data in meters

	print(lidar.scan.distances)	# print distance list
