import pytim5xx as lidar

for x in range(10):
	distances = lidar.scan()
	print(distances)
