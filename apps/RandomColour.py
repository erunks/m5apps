from utils.App import App

class RandomColour(App):
  def __init__(self):
    super().__init__()

    self.bh.press_func(self.set_random_color)
    # self.bh.release_func(pmh.clear_all())
    # self.bh.double_func(pmh.set_all())
    self.bh.long_func(self.pmh.clear_all)

  def set_random_color(self):
    from random import randint, random
    self.pmh.pixel_color(randint(0,359), random(), random())
    self.pmh.set_all()
