class PixelMatrixHelper:
  def __init__(self):
    from machine import Pin
    from neopixel import NeoPixel

    # Pin 27, is the pin used for the display matrix
    # https://docs.m5stack.com/en/core/atom_matrix
    # and we pass 25, to this, as there are 25 pixels total
    self.pixel_matrix = NeoPixel(Pin(27, Pin.OUT), 25)


  def set_screen(pixel_array):
    pass


# >>> from neopixel import NeoPixel
# >>> from machine import Pin
# >>> pin = Pin(27, Pin.OUT)
# >>> np = NeoPixel(pin, 25)
# >>> np[0] = (10, 0, 0)
# >>> np.write()
# >>> btnPin = Pin(39, Pin.IN)
# >>> while True:
# ...     if btnPin.value() == 1:
# ...         np[24] = (0,0,10)
# ...     else:
# ...         np[24] = (0,0,0)
# ...     np.write()
# ...     
# ... 
# >>> np[24] = (0,0,0)
# >>> np.write()
# >>> from machine import SoftI2C
# >>> i2c = SoftI2C(scl = Pin(21), sda = Pin(25))
# >>> i2c.scan()
# [104]
# >>> hex(104)
# '0x68'
# >>> 
