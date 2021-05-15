from external_modules.abutton import Pushbutton

class ButtonHelper(Pushbutton):
  def __init__(self):
    from machine import Pin

    # Pin 39, is the pin used for the button under the display matrix
    # https://docs.m5stack.com/en/core/atom_matrix
    super().__init__(Pin(39, Pin.IN))

  def getButtonValue(self):
    return self.rawstate()

  def getButtonPressed(self):
    return self.getButtonValue() == True
