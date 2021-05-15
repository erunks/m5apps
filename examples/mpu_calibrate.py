def run():
  from machine import SoftI2C, Pin
  from external_modules.mpu6886 import MPU6886

  i2c = SoftI2C(scl=Pin(21), sda=Pin(25))
  sensor = MPU6886(i2c)
  offset = sensor.calibrate(count=256, delay=0)

  print(offset)
