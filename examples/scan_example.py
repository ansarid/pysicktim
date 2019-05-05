# Import pytim5xx Library as "lidar"
import pytim5xx as lidar

# Repeat code nested in for loop 10 times
for x in range(10):
# while True:

	lidar.scan()	# Requests and returns list of LIDAR
					# distance information in meters

	print(lidar.scan.distances)		# print distance list
