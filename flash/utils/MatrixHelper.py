class MatrixHelper:
  def __init__(self, N = 5):
    self.N = N

  # An Inplace function to rotate
  # N x N matrix by 90 degrees in
  # anti-clockwise direction
  def rotateMatrix(self, mat):
    
    # Consider all squares one by one
    for x in range(0, int(self.N / 2)):
      
      # Consider elements in group
      # of 4 in current square
      for y in range(x, self.N-x-1):
        
        # store current cell in temp variable
        temp = mat[x+y]

        # move values from right to top
        mat[x+y] = mat[y+self.N-1-x]

        # move values from bottom to right
        mat[y+self.N-1-x] = mat[self.N-1-x+self.N-1-y]

        # move values from left to bottom
        mat[self.N-1-x+self.N-1-y] = mat[self.N-1-y+x]

        # assign temp to left
        mat[self.N-1-y+x] = temp

  def displayMatrix(self, mat):
    row = ""
    counter = 0
    for i in range(0, self.N * self.N):
      counter += 1
      row += "%d " % mat[i]
      if (counter >= 5):
        print("%s\n" % row)
        counter = 0
        row = ""
