# Example code for PiicoDev Motion Sensor MPU6050
from PiicoDev_MPU6050 import PiicoDev_MPU6050

from utime import sleep_ms

motion = PiicoDev_MPU6050()

while True:
    
    # Accelerometer data
    accel = motion.read_accel_data() # read the accelerometer [ms^-2]
    print("x:" + str(accel["x"]) + " y:" + str(accel["y"]) + " z:" + str(accel["z"]))
    
    # Gyroscope Data
#     gyro = motion.read_gyro_data()   # read the gyro [deg/s]
#     print("x:" + str(gyro["x"]) + " y:" + str(gyro["y"]) + " z:" + str(gyro["z"]))
    
    # Rough temperature
#     temp = motion.read_temperature()   # read the device temperature [degC]
#     print("Temperature: " + str(temp) + "°C")

    # G-Force
#     gforce = motion.read_accel_abs(g=True)
#     print("G-Force: " + str(gforce))
    
    sleep_ms(100)
