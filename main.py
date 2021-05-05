# Example code for PiicoDev Motion Sensor MPU6050
from PiicoDev_MPU6050 import PiicoDev_MPU6050

from utime import sleep_ms

motion = PiicoDev_MPU6050()

while True:
    accel = motion.get_accel() # read the accelerometer [ms^-2]
    gyro = motion.get_gyro()   # read the gyro [deg/s]
    temp = motion.get_temp()   # read the device temperature [degC]

    print("{}  {}  {}".format(accel, gyro, temp)) # print the data

    sleep_ms(100)
