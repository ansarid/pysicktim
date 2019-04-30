import pytim5xx as lidar

for x in range(10):
	telegram = lidar.scan()
	print(telegram)
