class App:
  def __init__(self):
    from utils.ButtonHelper import ButtonHelper
    from utils.PixelMatrixHelper import PixelMatrixHelper

    self.bh = ButtonHelper()
    self.pmh = PixelMatrixHelper()

  def run(self):
    self.bh.loop.run_forever()
