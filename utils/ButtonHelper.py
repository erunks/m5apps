from external_modules.abutton import Pushbutton

class ButtonHelper(Pushbutton):
  def __init__(self):
    from machine import Pin

    # Pin 39, is the pin used for the button under the display matrix
    # https://docs.m5stack.com/en/core/atom_matrix
    super().__init__(Pin(39, Pin.IN))

  def __del__(self):
    self.stop_checking = True
    try:
      self.loop.stop()
      self.loop.close()
      del self.pin
    finally:
      self.pin = None

  def getButtonValue(self):
    return self.rawstate()

  def getButtonPressed(self):
    return self.getButtonValue() == True
