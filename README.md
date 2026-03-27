# Maze Generator

Wrote a recursive backtracking algorithm  a depth-first approach that creates mazes.

- Configurable maze dimensions (must be odd numbers)
- Deterministic generation with random seed support
- Recursive backtracking implementation

#
The algorithm starts at a given cell and:
1. Carves out the current cell
2. Randomly selects an unvisited neighboring cell (two steps away)
3. Carves a path to that neighbor
4. Recursively visits the neighbor
5. Backtracks when reaching dead ends until all cells are visited

<strong>Took me 8hours to make this work, am dumb af</strong>

## TODO

- [ ] Add maze solver using BFS
- [ ] Implement DFS solver for comparison
- [ ] Export maze to image

##

```python
from maze_generator import GenMaze

# Create a 39x19 maze with seed 1, starting at (1, 1)
maze = GenMaze(39, 19, 1, 1, 1)

# Generate the maze
maze.visit(1, 1)

# Display the final maze
maze.printMaze(maze.getMaze())