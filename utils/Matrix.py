# Author: Edward Runkel
# Copyright Edward Runkel 2020-2021 Released under the MIT license
# Based on Dawid Stankiewicz's matrix.py. Rewritten as an inheritable
# class in Python3.
# Created on 2021-05-07

__updated__ = "2021-05-07"
__version__ = "2.0"

from external_modules.font import get_letter
from machine import Pin
from neopixel import NeoPixel
import time
import math

class Matrix:
  def __init__(self, INSTA_DRAW = True):
    # M5atom matrix hardware specific values
    self.LED_PIN = 27
    self.LED_WIDTH = 5
    self.LED_HEIGHT = 5
    self.LED_NUM = self.LED_WIDTH * self.LED_HEIGHT
    self.LED_BRIGHTNESS = 0.25 # Max led brightness due to heating up to high temperature
    self.INSTA_DRAW = INSTA_DRAW

    # Color in hsv color model color(h, s, v)
    # h: 0 to 360
    # s: 0.0 to 1.0
    # v: 0.0 to 1.0
    self.color = (0, 0, 1 * self.LED_BRIGHTNESS) # Initial set color to white

    self.np = NeoPixel(Pin(self.LED_PIN, Pin.OUT), self.LED_NUM)

  def translate(self, value, inMin, inMax, outMin, outMax):
    return (value - inMin) * (outMax - outMin) / (inMax - inMin) + outMin

  # Convert color from hsv to rgb
  def hsv(self, h, s=1, v=1):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b

  # Set color used to draw function
  def pixel_color(self, h, s=1, v=1):
    self.color = (h, s, v * self.LED_BRIGHTNESS)

  def pixel_set(self, x, y):
    self.np[x + y * self.LED_HEIGHT] = self.hsv(*self.color)
    if self.INSTA_DRAW: self.show()

  def pixel_clear(self, x, y):
    self.np[x + y * self.LED_HEIGHT] = (0, 0, 0)
    if self.INSTA_DRAW: self.show()

  def pixel_blink(self, x, y, delay_ms=100 ):
    previous = self.np[x + y * self.LED_HEIGHT]
    self.np[x + y * self.LED_HEIGHT] = self.hsv(*self.color)
    self.show()
    time.sleep_ms( delay_ms )
    self.np[x + y * self.LED_HEIGHT] = previous
    self.show()

  def clear_all(self):
    self.np.fill((0,0,0))
    if self.INSTA_DRAW: self.show()

  def set_all(self):
    self.np.fill(self.hsv(*self.color))
    if self.INSTA_DRAW: self.show()

  def show(self):
    self.np.write()

  # Write raw rgb value buffer to matrix
  def write_buffer(self, buf):
    size = self.LED_NUM
    if len(buf) < self.LED_NUM:
      size = len(buf)
    for pix in range (0, size):
      if buf[pix]: self.np[pix] = self.hsv(*self.color)
      else: self.np[pix] = self.hsv(0,0,0)
    if self.INSTA_DRAW: self.show()

  def pixel_breathe(self, x, y, ms_in=50, ms_out=50):
    for i in range (0, 11, 1):
      val = math.pow(2, i) - 1
      self.np[x + y * self.LED_HEIGHT] = self.hsv(self.color[0], self.color[1], (self.LED_BRIGHTNESS * self.translate(val, 0, 1024, 0, 1)) )
      self.show()
      time.sleep_ms(ms_in)
    for i in range (10, -1, -1):
      val = math.pow(2, i) - 1
      self.np[x + y * self.LED_HEIGHT] = self.hsv(self.color[0], self.color[1], (self.LED_BRIGHTNESS * self.translate(val, 0, 1024, 0, 1)) )
      self.show()
      time.sleep_ms(ms_out)

  def pixel_mask(self, buf):
    size = self.LED_NUM
    if len(buf) < self.LED_NUM:
      size = len(buf)
    for pix in range (0, size):
      if buf[pix]: self.np[pix] = self.hsv(*self.color)
      else: self.np[pix] = self.hsv(0,0,0)
    if self.INSTA_DRAW: self.show()
  
  def _add(self, a, b):
    w_a = int(len(a)/5)
    w_b = int(len(b)/5)
    out = [0] *len(a)
    for i in range(len(a)):
      out[i] = a[i]
    for i in range(5):
      out[(i*w_a+i*w_b):(i*w_a+i*w_b)] = b[(i*w_b):((i+1)*w_b)]
    return out

  def _get_frame(self, buffer, offest):
    w_buf = int(len(buffer)/5)
    out = [0] *25
    for x in range (5):
      for y in range (5):
        out[x + y * 5] = buffer[(x+offest)+(y*w_buf)]
    return out

  def _create_pixmap(self, input):
    spacer = [0] *5
    empty = [0] *25
    text_buffer = [0] *25
    for i in range (len(input)):
      text_buffer = self._add(text_buffer, get_letter( ord( input[len(input)-1-i] ) ) )
      text_buffer = self._add(text_buffer, spacer) 
    text_buffer = self._add(text_buffer, empty)
    return text_buffer

  def text_scroll(self, text_to_scroll, delay=150):
    t_buf = self._create_pixmap(text_to_scroll)
    # Scrolling pixmap on matrix
    for pos in range ( int(len(t_buf)/5) -5 +1 ):
      self.clear_all()
      self.pixel_mask(self._get_frame(t_buf, pos) )
      self.show()
      time.sleep_ms(delay)


