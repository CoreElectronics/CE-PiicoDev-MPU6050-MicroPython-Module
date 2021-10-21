_G='NaN'
_F=True
_E=None
_D=False
_C='z'
_B='y'
_A='x'
from PiicoDev_Unified import *
from math import sqrt
from time import sleep
compat_str='\nUnified PiicoDev library out of date.  Get the latest module: https://piico.dev/unified \n'
_GRAVITIY_MS2=9.80665
_ACC_SCLR_2G=16384.0
_ACC_SCLR_4G=8192.0
_ACC_SCLR_8G=4096.0
_ACC_SCLR_16G=2048.0
_GYR_SCLR_250DEG=131.0
_GYR_SCLR_500DEG=65.5
_GYR_SCLR_1000DEG=32.8
_GYR_SCLR_2000DEG=16.4
_ACC_RNG_2G=0
_ACC_RNG_4G=8
_ACC_RNG_8G=16
_ACC_RNG_16G=24
_GYR_RNG_250DEG=0
_GYR_RNG_500DEG=8
_GYR_RNG_1000DEG=16
_GYR_RNG_2000DEG=24
_PWR_MGMT_1=107
_ACCEL_XOUT0=59
_TEMP_OUT0=65
_GYRO_XOUT0=67
_ACCEL_CONFIG=28
_GYRO_CONFIG=27
_maxFails=3
_MPU6050_ADDRESS=104
def signedIntFromBytes(x,endian='big'):
	y=int.from_bytes(x,endian)
	if y>=32768:return-(65535-y+1)
	else:return y
class PiicoDev_MPU6050:
	def __init__(self,bus=_E,freq=_E,sda=_E,scl=_E,addr=_MPU6050_ADDRESS):
		self._failCount=0;self._terminatingFailCount=0
		try:
			if compat_ind>=1:0
			else:print(compat_str)
		except:print(compat_str)
		self.i2c=create_unified_i2c(bus=bus,freq=freq,sda=sda,scl=scl);self.addr=addr
		try:self.i2c.writeto_mem(self.addr,_PWR_MGMT_1,bytes([0]));sleep_ms(5)
		except Exception as e:print(i2c_err_str.format(self.addr));raise e
		self._accel_range=self.get_accel_range(_F);self._gyro_range=self.get_gyro_range(_F)
	def _readData(self,register):
		failCount=0
		while failCount<_maxFails:
			try:sleep_ms(10);data=self.i2c.readfrom_mem(self.addr,register,6);break
			except:
				failCount=failCount+1;self._failCount=self._failCount+1
				if failCount>=_maxFails:self._terminatingFailCount=self._terminatingFailCount+1;print(i2c_err_str.format(self.addr));return{_A:float(_G),_B:float(_G),_C:float(_G)}
		x=signedIntFromBytes(data[0:2]);y=signedIntFromBytes(data[2:4]);z=signedIntFromBytes(data[4:6]);return{_A:x,_B:y,_C:z}
	def read_temperature(self):
		try:rawData=self.i2c.readfrom_mem(self.addr,_TEMP_OUT0,2);raw_temp=signedIntFromBytes(rawData,'big')
		except:print(i2c_err_str.format(self.addr));return float(_G)
		actual_temp=raw_temp/340+36.53;return actual_temp
	def set_accel_range(self,accel_range):self.i2c.writeto_mem(self.addr,_ACCEL_CONFIG,bytes([accel_range]));self._accel_range=accel_range
	def get_accel_range(self,raw=_D):
		raw_data=self.i2c.readfrom_mem(self.addr,_ACCEL_CONFIG,2)
		if raw is _F:return raw_data[0]
		elif raw is _D:
			if raw_data[0]==_ACC_RNG_2G:return 2
			elif raw_data[0]==_ACC_RNG_4G:return 4
			elif raw_data[0]==_ACC_RNG_8G:return 8
			elif raw_data[0]==_ACC_RNG_16G:return 16
			else:return-1
	def read_accel_data(self,g=_D):
		accel_data=self._readData(_ACCEL_XOUT0);accel_range=self._accel_range;scaler=_E
		if accel_range==_ACC_RNG_2G:scaler=_ACC_SCLR_2G
		elif accel_range==_ACC_RNG_4G:scaler=_ACC_SCLR_4G
		elif accel_range==_ACC_RNG_8G:scaler=_ACC_SCLR_8G
		elif accel_range==_ACC_RNG_16G:scaler=_ACC_SCLR_16G
		else:print('Unkown range - scaler set to _ACC_SCLR_2G');scaler=_ACC_SCLR_2G
		x=accel_data[_A]/scaler;y=accel_data[_B]/scaler;z=accel_data[_C]/scaler
		if g is _F:return{_A:x,_B:y,_C:z}
		elif g is _D:x=x*_GRAVITIY_MS2;y=y*_GRAVITIY_MS2;z=z*_GRAVITIY_MS2;return{_A:x,_B:y,_C:z}
	def read_accel_abs(self,g=_D):d=self.read_accel_data(g);return sqrt(d[_A]**2+d[_B]**2+d[_C]**2)
	def set_gyro_range(self,gyro_range):self.i2c.writeto_mem(self.addr,_GYRO_CONFIG,bytes([gyro_range]));self._gyro_range=gyro_range
	def get_gyro_range(self,raw=_D):
		raw_data=self.i2c.readfrom_mem(self.addr,_GYRO_CONFIG,2)
		if raw is _F:return raw_data[0]
		elif raw is _D:
			if raw_data[0]==_GYR_RNG_250DEG:return 250
			elif raw_data[0]==_GYR_RNG_500DEG:return 500
			elif raw_data[0]==_GYR_RNG_1000DEG:return 1000
			elif raw_data[0]==_GYR_RNG_2000DEG:return 2000
			else:return-1
	def read_gyro_data(self):
		gyro_data=self._readData(_GYRO_XOUT0);gyro_range=self._gyro_range;scaler=_E
		if gyro_range==_GYR_RNG_250DEG:scaler=_GYR_SCLR_250DEG
		elif gyro_range==_GYR_RNG_500DEG:scaler=_GYR_SCLR_500DEG
		elif gyro_range==_GYR_RNG_1000DEG:scaler=_GYR_SCLR_1000DEG
		elif gyro_range==_GYR_RNG_2000DEG:scaler=_GYR_SCLR_2000DEG
		else:print('Unkown range - scaler set to _GYR_SCLR_250DEG');scaler=_GYR_SCLR_250DEG
		x=gyro_data[_A]/scaler;y=gyro_data[_B]/scaler;z=gyro_data[_C]/scaler;return{_A:x,_B:y,_C:z}