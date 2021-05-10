from rplidar import RPLidar
lidar = RPLidar('/dev/ttyUSB0')

# info = lidar.get_info()
# print(info)

# health = lidar.get_health()
# print(health)
 
lidar.stop()
lidar.stop_motor()
lidar.disconnect()