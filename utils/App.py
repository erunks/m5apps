import uasyncio as asyncio
class App:
  def __init__(self):
    from utils.ButtonHelper import ButtonHelper
    from utils.MpuHelper import MpuHelper
    from utils.PixelMatrixHelper import PixelMatrixHelper

    self.bh = ButtonHelper()
    self.mh = MpuHelper()
    self.pmh = PixelMatrixHelper()
    self.loop = asyncio.get_event_loop()
    self.loop.create_task(self.poll())

  async def poll(self):
    while True:
      self.bh.buttoncheck()
      self.mh.read_gyro()
      await asyncio.sleep_ms(50)

  def run(self):
    self.loop.run_forever()
