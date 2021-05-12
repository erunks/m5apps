def run():
  import utime
  from machine import SoftI2C, Pin
  from external_modules.mpu6886 import MPU6886

  i2c = SoftI2C(scl=Pin(21), sda=Pin(25))
  sensor = MPU6886(i2c, offset=(0.00577786, -0.002606334, 0.002436151))

  print("MPU6886 id: " + hex(sensor.whoami))

  while True:
    print(sensor.acceleration)
    print(sensor.gyro)
    print(sensor.temperature)

    utime.sleep_ms(1000)
