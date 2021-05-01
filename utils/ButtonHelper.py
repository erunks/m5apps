class ButtonHelper:
  def __init__(self):
    from machine import Pin

    # Pin 39, is the pin used for the button under the display matrix
    # https://docs.m5stack.com/en/core/atom_matrix
    self.btn = Pin(39, Pin.IN)

  # returns 0 when button is pressed down
  # returns 1 when button is not pressed
  def getButtonValue(self):
    return self.btn.value()

  def getButtonPressed(self):
    return self.getButtonValue() == 0