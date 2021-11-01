# PiicoDev® MPU6050 MicroPython Module

This is the firmware repo for the [Core Electronics PiicoDev® Motion Sensor MPU-6050](https://core-electronics.com.au/catalog/product/view/sku/CE07822)

This module depends on the [PiicoDev Unified Library](https://github.com/CoreElectronics/CE-PiicoDev-Unified). Place `PiicoDev_Unified.py` in the same directory.

See the Quickstart Guides:
- [Micro:bit v2](https://core-electronics.com.au/tutorials/piicodev-motion-sensor-mpu-6050-micro-bit-guide.html)
- [Raspberry Pi Pico](https://core-electronics.com.au/tutorials/piicodev-motion-sensor-mpu-6050-raspberry-pi-pico-guide.html)
- [Raspberry Pi](https://core-electronics.com.au/tutorials/piicodev-motion-sensor-mpu-6050-raspberry-pi-guide.html)

# Usage
## Example
[main.py](https://github.com/CoreElectronics/CE-PiicoDev-MPU6050-MicroPython-Module/blob/main/main.py) is a simple example to get started.
```
# Example code for PiicoDev Motion Sensor MPU6050
from PiicoDev_MPU6050 import PiicoDev_MPU6050

from time import sleep

motion = PiicoDev_MPU6050()

while True:

    # Accelerometer data
    accel = motion.read_accel_data() # read the accelerometer [ms^-2]
    aX = accel["x"]
    aY = accel["y"]
    aZ = accel["z"]
    print("x:" + str(aX) + " y:" + str(aY) + " z:" + str(aZ))

    # Gyroscope Data
    gyro = motion.read_gyro_data()   # read the gyro [deg/s]
    gX = gyro["x"]
    gY = gyro["y"]
    gZ = gyro["z"]
    print("x:" + str(gX) + " y:" + str(gY) + " z:" + str(gZ))

    # Rough temperature
    temp = motion.read_temperature()   # read the device temperature [degC]
    print("Temperature: " + str(temp) + "°C")

    # G-Force
    gforce = motion.read_accel_abs(g=True) # read the absolute acceleration magnitude
    print("G-Force: " + str(gforce))

    sleep(0.1)
```
## Details
### PiicoDev_MPU6050(bus=, freq=, sda=, scl=, address=0x68)

Parameter | Type | Range | Default | Description
--- | --- | --- | --- | ---
bus | int | 0,1 | Raspberry Pi Pico: 0, Raspberry Pi: 1 | I2C Bus.  Ignored on Micro:bit
freq | int | 100-1000000 | Device dependent | I2C Bus frequency (Hz).  Ignored on Raspberry Pi
sda | Pin | Device Dependent | Device Dependent | I2C SDA Pin. Implemented on Raspberry Pi Pico only
scl | Pin | Device Dependent | Device Dependent | I2C SCL Pin. Implemented on Raspberry Pi Pico only
address | int | 0x68, 0x69 | 0x68 | This address needs to match the PiicoDev Motion Sensor MPU6050 hardware address configured by the jumper or ADR pin

### PiicoDev_MPU6050.read_accel_data(g=False)
Returns a dictionary `x` `y` `z`

Parameter | Type | Default | Description | Unit
--- | --- | --- | --- | ---
g | bool |  False | If False, retuned units are m/s.  If True, returned units are g
returned x | float | |x acceleration | g or m/s
returned y | float | | y acceleration | g or m/s
returned z | float | |z acceleration | g or m/s

### PiicoDev_MPU6050.read_accel_abs(g=False)
Parameter | Type | Default | Description | Unit
--- | --- | --- | --- | ---
g | bool |  False | If False, retuned units are m/s.  If True, returned units are g
returned | float | | Acceleration magnitude | g or m/s

### PiicoDev_MPU6050.read_gyro_data()
Returns a dictionary `x` `y` `z`

Parameter | Type | Description | Unit
--- | --- | --- | ---
returned x | float | x value from gyroscope | deg/s
returned y | float | y value from gyroscope | deg/s
returned z | float | z value from gyroscope | deg/s

### PiicoDev_MPU6050.read_temperature()

Parameter | Type | Description | Unit
--- | --- | --- | ---
returned | float | Temperature | degC

### PiicoDev_MPU6050.get_accel_range(raw=False)
Parameter | Type | Default | Description | Unit
--- | --- | --- | --- | ---
raw | bool |  False | If False, returned ranger is integer: -1, 2, 4, 8 or 16.  If True, returned range is the raw value from the ACCEL_CONFIG register
returned | int | | Accelerometer range | #

### PiicoDev_MPU6050.set_accel_range(accel_range)
Parameter | Type | Description
--- | --- | ---
accel_range | int | the range to set the accelerometer to. Using a pre-defined range from the [MPU-6050 datasheet](https://invensense.tdk.com/wp-content/uploads/2015/02/MPU-6000-Datasheet1.pdf) is advised.

### PiicoDev_MPU6050.get_gyro_range(raw=False)
Parameter | Type | Default | Description | Unit
--- | --- | --- | --- | ---
raw | bool |  False | If False, returned range is deg/s.  If True, returned range is the raw value from GYRO_CONFIG register
returned | int | | Gyro range | #

### PiicoDev_MPU6050.set_gyro_range(gyro_range)
Parameter | Type | Description
--- | --- | ---
gyro_range |  int | The range to set the gyro to. Using a pre-defined range from the [MPU-6050 datasheet](https://invensense.tdk.com/wp-content/uploads/2015/02/MPU-6000-Datasheet1.pdf) is advised.

### PiicoDev_MPU6050.read_angle()
Returns a dictionary `x` `y`
Parameter | Type | Description
--- | --- | ---
returned x |  float | Radians: The tilt angle about the x-axis. Refer to silkscreen axes
returned y |  float | Radians: The tilt angle about the y-axis. Refer to silkscreen axes


# License
This project is open source - please review the LICENSE.md file for further licensing information.

If you have any technical questions, or concerns about licensing, please contact technical support on the [Core Electronics forums](https://forum.core-electronics.com.au/).

*\"PiicoDev\" and the PiicoDev logo are trademarks of Core Electronics Pty Ltd.*
