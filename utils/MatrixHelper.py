class MatrixHelper:
  def __init__(self, N = 5):
    self.N = N

  def _calculateNewPosition(self, index):
    from math import floor

    x = index % self.N
    y = floor(index / self.N)
    newX = self.N - y - 1
    newY = x
    return newY * self.N + newX

  def displayMatrix(self, mat):
    row = ""
    counter = 0
    for i in range(0, self.N * self.N):
      counter += 1
      row += "%X " % mat[i]
      if (counter >= 5):
        print("%s" % row)
        counter = 0
        row = ""

  def rotateMatrixClockwise(self, mat):
    rotated = [None] * len(mat)
    for i in range(self.N * self.N):
      newPos = self._calculateNewPosition(i)
      rotated[newPos] = mat[i]
    return rotated
