from os.path import normpath 
from levels.level.lvl1_field import Field
from queue import Queue

def pathfinder(start):
    frontier = Queue()
    frontier.put(start )
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == goal: 
            break           

        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current