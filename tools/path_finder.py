from os.path import normpath
from queue import PriorityQueue, Queue
from levels.level.lvl1_field import Field
from tools.utils import heuristic


def pathfinder(start, goal):
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None
    graph = Graph()

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break
        
        for next in graph.neighbors(current):
            if next not in came_from:
                priority = heuristic(next, goal)
                frontier.put(next)
                came_from[next] = current
    
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


class Graph:
    def __init__(self):
        self.field = Field

    def neighbors(self, current):
        i, j  = current
        
        exit = []
        if i > 0 and self.field[i-1][j] != -1:
            exit.append((i-1, j))
        if i < len(self.field)-1 and self.field[i+1][j] != -1:
            exit.append((i+1, j))
        if j > 0 and self.field[i][j-1] != -1:
            exit.append((i, j-1))
        if j < len(self.field[0])-1 and self.field[i][j+1] != -1:
            exit.append((i, j+1))
        return exit

pathfinder((5,5), (10,10))