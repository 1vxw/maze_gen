import random

class GenMaze():
  MARK = '@'
  EMPTY = ' '
  UP, DOWN, LEFT, RIGHT = 'u','d','l','r'
  WALL = chr(9608)

  def __init__(self, W, H, SEED, x, y):
      self.height = H
      self.width = W
      self.seed = SEED
      self.x = x
      self.y = y

      random.seed(self.seed)

      self.visited = [(x,y)]

      self.maze = [[self.WALL for _ in range(self.height)] for _ in range(self.width)]
      self.maze[x][y] = self.EMPTY


  def printMaze(self, maze, markX = None, markY = None):
      for y in range(self.height):
        for x in range(self.width):
          if markX == x and markY == y:
            print(self.MARK, end="")
          else:
            print(maze[x][y], end="")
        print()

  def getMaze(self):
    return self.maze

  def getX(self):
    return self.x

  def getY(self):
    return self.y

  def visit(self, x, y):
    self.maze[x][y] = self.EMPTY

    while True:
      unvN = []

      if y > 1 and (x, y-2) not in self.visited:
        unvN.append(self.UP)

      if y < self.height - 2 and (x, y+2) not in self.visited:
        unvN.append(self.DOWN)

      if x > 1 and (x - 2, y) not in self.visited:
        unvN.append(self.LEFT)

      if x < self.width - 2 and (x + 2,y) not in self.visited:
        unvN.append(self.RIGHT)

      if len(unvN) == 0:
        return
      
      else:
        nextIntersection = random.choice(unvN)

        match nextIntersection:
          case self.UP:
            nextX = x
            nextY = y - 2
            self.maze[x][y-1] = self.EMPTY
          case self.DOWN:
            nextX = x
            nextY = y + 2
            self.maze[x][y+1] = self.EMPTY
          case self.LEFT:
            nextX = x - 2
            nextY = y
            self.maze[x - 1][y] = self.EMPTY
          case self.RIGHT:
            nextX = x + 2
            nextY = y 
            self.maze[x + 1][y] = self.EMPTY
          case _: 
            raise ValueError(f"Invalid direction: {nextIntersection}")

        self.visited.append((nextX, nextY))
        self.visit(nextX, nextY)

x = GenMaze(39,19,30,1,1)  
x.visit(x.getX(), x.getY())
x.printMaze(x.getMaze())