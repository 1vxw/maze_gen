import random

class Node():
  def __init__(self, s, p, a):
    self.state = s
    self.parent = p
    self.action = a

class StackFrontier():
  def __init__(self):
    self.frontier = []

  def add(self, node):
    self.frontier.append(node)

  def empty(self):
    return len(self.frontier) == 0


  def contain_state(self, state):
    return any(node.state == state for node in self.frontier)

  def remove(self):
    if self.empty():
      raise Exception("empty frontier")

    node = self.frontier[-1]
    self.frontier = self.frontier[:-1]
    return node

class QueueFrontier(StackFrontier):
  def remove(self):
    if self.empty():
      raise Exception("empty frontier")

    node = self.frontier[0]
    self.frontier = self.frontier[1:]
    return node

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

      self.num_explored = 0
      self.start = (self.x, self.y)
      self.goal = (self.width - 2, self.height - 2) 

      self.explored = set()
      self.solution = set()

  def printMaze(self, maze, show_start=True, show_goal=True):
    for y in range(self.height):
        for x in range(self.width):
            if show_start and (x, y) == self.start:
                print('S', end="")  
            elif show_goal and (x, y) == self.goal:
                print('G', end="")  
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

  def neighbors(self, state):
    curr_x, curr_y = state
    candidates = []

    if curr_y > 0 and self.maze[curr_x][curr_y - 1] != self.WALL:
      candidates.append((self.UP, (curr_x, curr_y - 1)))

    if curr_y < self.height - 1 and self.maze[curr_x][curr_y + 1] != self.WALL:
      candidates.append((self.DOWN, (curr_x, curr_y + 1)))

    if curr_x > 0 and self.maze[curr_x - 1][curr_y] != self.WALL:
      candidates.append((self.LEFT, (curr_x - 1, curr_y)))

    if curr_x < self.width - 1 and self.maze[curr_x + 1][curr_y] != self.WALL:
      candidates.append((self.RIGHT, (curr_x + 1, curr_y)))

    return candidates

  def solve(self):
    self.num_explored = 0
    self.explored = set()
      
    start_node = Node(self.start, p=None, a=None)
    frontier = StackFrontier()
    frontier.add(start_node)

    self.explored.add(self.start)

    while True:
      if frontier.empty():
        raise Exception("no solution")

      node = frontier.remove()
      self.num_explored += 1
    
      if node.state == self.goal:
        actions = []
        cells = []

        while node.parent is not None:
          actions.append(node.action)
          cells.append(node.state)
          node = node.parent

        actions.reverse()
        cells.reverse()
        self.solution = (actions, cells)
        return

      for action, state in self.neighbors(node.state):
        if not frontier.contain_state(state) and state not in self.explored:
          child = Node(s=state, p=node, a=action)
          frontier.add(child)
          self.explored.add(state)
          
  def printSolution(self):
    if maze.solution:
      actions, cells = maze.solution
      print(f"Found solution, Path length: {len(actions)}")
      
      maze_copy = [row[:] for row in maze.getMaze()] 
      for cell in cells:
          if cell != maze.start and cell != maze.goal:
              x, y = cell
              if 0 <= x < len(maze_copy) and 0 <= y < len(maze_copy[0]):
                  maze_copy[x][y] = '.' 
      
      print("\nMaze with solution path:")
      for y in range(maze.height):
          for x in range(maze.width):
              if (x, y) == maze.start:
                  print('S', end="")
              elif (x, y) == maze.goal:
                  print('G', end="")
              else:
                  print(maze_copy[x][y], end="")
          print()
    else:
        print("No solution found!")

width, height = 39, 19
start_x, start_y = 1, 1
seed = 38

maze = GenMaze(width, height, seed, start_x, start_y)

maze.visit(maze.getX(), maze.getY())

maze.printMaze(maze.getMaze())

maze.solve()
maze.printSolution()
