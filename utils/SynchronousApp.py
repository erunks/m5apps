import time

class SynchronousApp:
  def __init__(self):
    from utils.ButtonHelper import ButtonHelper
    from utils.MpuHelper import MpuHelper
    from utils.PixelMatrixHelper import PixelMatrixHelper

    self.bh = ButtonHelper()
    self.mh = MpuHelper()
    self.pmh = PixelMatrixHelper()
    
  def poll(self):
    while True:
      self.bh.buttoncheck_sync()
      self.mh.read_gyro()
      time.sleep(0.5)
  
  def release_helpers(self):
    try:
      del self.bh
      del self.mh
      del self.pmh
    finally:
      self.bh = None
      self.mh = None
      self.pmh = None

  def run(self):
    print('Start %s' % self.__class__.__name__)
    self.poll()
