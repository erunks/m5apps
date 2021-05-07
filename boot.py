# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
#import webrepl
#webrepl.start()

from utils.ButtonHelper import ButtonHelper
from utils.PixelMatrixHelper import PixelMatrixHelper
bh = ButtonHelper()
pmh = PixelMatrixHelper()


def set_random_color():
  from random import randint
  pmh.pixel_color(randint(0,359), 1, 0.5)

pmh.pixel_color(240,1,0.5)
pmh.set_all()

bh.press_func(set_random_color())
# bh.release_func(pmh.clear_all())
bh.double_func(pmh.set_all())
bh.long_func(pmh.clear_all())

bh.loop.run_forever()
