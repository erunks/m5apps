from utils.App import App

class RotateArrow(App):
  def __init__(self):
    super().__init__()
    
    self.ARROW = [
      0,0,1,0,0,
      0,1,1,1,0,
      1,1,1,1,1,
      0,1,1,1,0,
      0,1,1,1,0
    ]

    self.CORNER_ARROW = [
      0,1,1,1,1,
      0,0,1,1,1,
      0,1,1,1,1,
      1,1,1,0,1,
      1,1,0,0,0,
    ]

    self.pointing_direction = 0
    self.pmh.pixel_color(0, 0, 0.125)
    self.pmh.write_buffer(self.ARROW)
    self.pmh.show()

  def _get_rotated_arrow(self, rotation):
    if rotation == 0: return self.ARROW
    if rotation == 0.5: return self.CORNER_ARROW

    rotatedArrow = self.ARROW if isinstance(rotation, int) else self.CORNER_ARROW
    for i in range(0, int(rotation)):
      rotatedArrow = self.pmh.rotateMatrixClockwise(rotatedArrow)

    return rotatedArrow

  async def poll(self):
    import uasyncio as asyncio
    while True:
      self.bh.buttoncheck()
      await self.mh.read_gyro()
      await self.rotateArrow()
      await asyncio.sleep_ms(50)

  async def rotateArrow(self):
    if self.mh.level: pass
    if self.mh.current_tilt_direction != self.pointing_direction:
      self.pointing_direction = self.mh.current_tilt_direction
      self.pmh.write_buffer(self._get_rotated_arrow(self.pointing_direction))
      self.pmh.show()
