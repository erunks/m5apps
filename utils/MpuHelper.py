class MpuHelper:
  def __init__(self):
    from machine import SoftI2C, Pin
    from external_modules.mpu6886 import MPU6886

    i2c = SoftI2C(scl=Pin(21), sda=Pin(25))

    self.sensor = MPU6886(i2c, gyro_offset=(-0.01894172, -0.01216358, -2.179874))
    self.current_tilt_direction = 0 # Using CSS mapping 0 through 3 = Up, Right, Down, Left 
    self.tilt_table = {
      'X': 0,
      'Y': 0,
      'Z': 0
    }

  def _update_current_tilt_direction(self):
    if self.tilt_table['Y'] == -1 and self.tilt_table['X'] == 1: self.current_tilt_direction = 0.5
    elif self.tilt_table['Y'] == 1 and self.tilt_table['X'] == 1: self.current_tilt_direction = 1.5
    elif self.tilt_table['Y'] == 1 and self.tilt_table['X'] == -1: self.current_tilt_direction = 2.5
    elif self.tilt_table['Y'] == -1 and self.tilt_table['X'] == -1: self.current_tilt_direction = 3.5
    elif self.tilt_table['Y'] == -1: self.current_tilt_direction = 0
    elif self.tilt_table['X'] == 1: self.current_tilt_direction = 1
    elif self.tilt_table['Y'] == 1: self.current_tilt_direction = 2
    elif self.tilt_table['X'] == -1: self.current_tilt_direction = 3

  def _update_tilt_table(self, key, value):
    if value >= 1.0: self.tilt_table[key] = 1
    elif value <= -1.0: self.tilt_table[key] = -1
    else: self.tilt_table[key] = 0

  @property
  def level(self):
    return self.tilt_table['X'] == 0 and self.tilt_table['Y'] == 0

  async def read_gyro(self):
    # GYRO (X,Y,Z)
    #
    # X,Y,Z Floats ranging from -2.2 to 2.2
    # Trigger threshold should be considered half -1.1 to 1.1
    #
    # Tilted Up: (_, -Y, _)
    # Tilted Down: (_, +Y, _)
    # Tilted Left: (-X, _, _)
    # Tilted Right: (+X, _, _)
    # Face Up: (_, _, -Z)
    # Face Down: (_, _, +Z)

    X,Y,Z = self.sensor.gyro

    self._update_tilt_table('X', X)
    self._update_tilt_table('Y', Y)
    self._update_tilt_table('Z', Z)
    self._update_current_tilt_direction()
