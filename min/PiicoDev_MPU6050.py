_G=True
_F='z'
_E='y'
_D='x'
_C=False
_B='NaN'
_A=None
from PiicoDev_Unified import *
from math import sqrt
from time import sleep
compat_str='\nUnified PiicoDev library out of date.  Get the latest module: https://piico.dev/unified \n'
_MPU6050_ADDRESS=104
class PiicoDev_MPU6050:
	GRAVITIY_MS2=9.80665;ACC_SCLR_2G=16384.0;ACC_SCLR_4G=8192.0;ACC_SCLR_8G=4096.0;ACC_SCLR_16G=2048.0;GYR_SCLR_250DEG=131.0;GYR_SCLR_500DEG=65.5;GYR_SCLR_1000DEG=32.8;GYR_SCLR_2000DEG=16.4;ACC_RNG_2G=0;ACC_RNG_4G=8;ACC_RNG_8G=16;ACC_RNG_16G=24;GYR_RNG_250DEG=0;GYR_RNG_500DEG=8;GYR_RNG_1000DEG=16;GYR_RNG_2000DEG=24;PWR_MGMT_1=107;PWR_MGMT_2=108;SELF_TEST_X=13;SELF_TEST_Y=14;SELF_TEST_Z=15;SELF_TEST_A=16;ACCEL_XOUT0=59;ACCEL_XOUT1=60;ACCEL_YOUT0=61;ACCEL_YOUT1=62;ACCEL_ZOUT0=63;ACCEL_ZOUT1=64;TEMP_OUT0=65;TEMP_OUT1=66;GYRO_XOUT0=67;GYRO_XOUT1=68;GYRO_YOUT0=69;GYRO_YOUT1=70;GYRO_ZOUT0=71;GYRO_ZOUT1=72;ACCEL_CONFIG=28;GYRO_CONFIG=27
	def __init__(self,bus=_A,freq=_A,sda=_A,scl=_A,addr=_MPU6050_ADDRESS):
		try:
			if compat_ind>=1:0
			else:print(compat_str)
		except:print(compat_str)
		self.i2c=create_unified_i2c(bus=bus,freq=freq,sda=sda,scl=scl);self.addr=addr
		for i in range(0,3):
			try:self.i2c.write8(self.addr,bytes([self.PWR_MGMT_1]),bytes([0]));sleep(0.005);break
			except Exception:print('Device 0x{:02X} not found, trying again'.format(self.addr));sleep(0.005)
	def read_i2c_word(self,register_high):
		rawData=self.i2c.readfrom_mem(self.addr,register_high,2);value=int.from_bytes(rawData,'big')
		if value>=32768:return-(65535-value+1)
		else:return value
	def read_temperature(self):
		try:raw_temp=self.read_i2c_word(self.TEMP_OUT0)
		except:print(i2c_err_str.format(self.addr));return float(_B)
		actual_temp=raw_temp/340+36.53;return actual_temp
	def set_accel_range(self,accel_range):self.i2c.write8(self.addr,bytes([self.ACCEL_CONFIG]),bytes([0]));self.i2c.write8(self.addr,bytes([self.ACCEL_CONFIG]),bytes([accel_range]))
	def get_accel_range(self,raw=_C):
		raw_data=self.i2c.read16(self.addr,bytes([self.ACCEL_CONFIG]))
		if raw is _G:return raw_data[0]
		elif raw is _C:
			if raw_data[0]==self.ACC_RNG_2G:return 2
			elif raw_data[0]==self.ACC_RNG_4G:return 4
			elif raw_data[0]==self.ACC_RNG_8G:return 8
			elif raw_data[0]==self.ACC_RNG_16G:return 16
			else:return-1
	def read_accel_data(self,g=_C):
		try:x=self.read_i2c_word(self.ACCEL_XOUT0);y=self.read_i2c_word(self.ACCEL_YOUT0);z=self.read_i2c_word(self.ACCEL_ZOUT0)
		except:print(i2c_err_str.format(self.addr));return{_D:float(_B),_E:float(_B),_F:float(_B)}
		scaler=_A;scaler=_A;accel_range=self.get_accel_range(_G)
		if accel_range==self.ACC_RNG_2G:scaler=self.ACC_SCLR_2G
		elif accel_range==self.ACC_RNG_4G:scaler=self.ACC_SCLR_4G
		elif accel_range==self.ACC_RNG_8G:scaler=self.ACC_SCLR_8G
		elif accel_range==self.ACC_RNG_16G:scaler=self.ACC_SCLR_16G
		else:print('Unkown range - scaler set to self.ACC_SCLR_2G');scaler=self.ACC_SCLR_2G
		x=x/scaler;y=y/scaler;z=z/scaler
		if g is _G:return{_D:x,_E:y,_F:z}
		elif g is _C:x=x*self.GRAVITIY_MS2;y=y*self.GRAVITIY_MS2;z=z*self.GRAVITIY_MS2;return{_D:x,_E:y,_F:z}
	def read_accel_abs(self,g=_C):d=self.read_accel_data(g);return sqrt(d[_D]**2+d[_E]**2+d[_F]**2)
	def set_gyro_range(self,gyro_range):self.i2c.write8(self.addr,bytes([self.GYRO_CONFIG]),bytes([0]));self.i2c.write8(self.addr,bytes([self.GYRO_CONFIG]),bytes([gyro_range]))
	def get_gyro_range(self,raw=_C):
		raw_data=self.i2c.read16(self.addr,bytes([self.GYRO_CONFIG]))
		if raw is _G:return raw_data[0]
		elif raw is _C:
			if raw_data[0]==self.GYR_RNG_250DEG:return 250
			elif raw_data[0]==self.GYR_RNG_500DEG:return 500
			elif raw_data[0]==self.GYR_RNG_1000DEG:return 1000
			elif raw_data[0]==self.GYR_RNG_2000DEG:return 2000
			else:return-1
	def read_gyro_data(self):
		try:x=self.read_i2c_word(self.GYRO_XOUT0);y=self.read_i2c_word(self.GYRO_YOUT0);z=self.read_i2c_word(self.GYRO_ZOUT0)
		except:print(i2c_err_str.format(self.addr));return{_D:float(_B),_E:float(_B),_F:float(_B)}
		scaler=_A;gyro_range=self.get_gyro_range(_G)
		if gyro_range==self.GYR_RNG_250DEG:scaler=self.GYR_SCLR_250DEG
		elif gyro_range==self.GYR_RNG_500DEG:scaler=self.GYR_SCLR_500DEG
		elif gyro_range==self.GYR_RNG_1000DEG:scaler=self.GYR_SCLR_1000DEG
		elif gyro_range==self.GYR_RNG_2000DEG:scaler=self.GYR_SCLR_2000DEG
		else:print('Unkown range - scaler set to self.GYR_SCLR_250DEG');scaler=self.GYR_SCLR_250DEG
		x=x/scaler;y=y/scaler;z=z/scaler;return{_D:x,_E:y,_F:z}