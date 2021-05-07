from utils.MatrixHelper import MatrixHelper

class PixelMatrixHelper(MatrixHelper):
  def __init__(self):
    # Pin 27, is the pin used for the display matrix
    # https://docs.m5stack.com/en/core/atom_matrix
    # and we pass 25, to this, as there are 25 pixels total
    
    super().__init__()

  def getNeoPixelArray(self):
    arr = []
    for i in range(0, self.N * self.N):
      arr.append(self.np[i])

    return arr
