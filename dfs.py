'''
Not being tested

from abc import abstractmethod, ABC
from collections import deque
from enum import IntEnum
import numpy as np

class Base(ABC):
    def __init__(self):
        self._container = deque()
    
    @abstractmethod
    def push(self, value):
        """push items"""
    
    @abstractmethod
    def pop(self):
        """pop items"""
    
    def __len__(self):
        return len(self._container)
    
    def __repr__(self):
        return f'{type(self).__name__}({list(self._container)})'

class Stack(Base):
    def push(self, value):
        self._container.append(value)
    
    def pop(self, value):
        return self._container.pop()
''' '''DFS section''''''
def dfs(initial, _next=successor, _test=test_goal):
    s: Stack = Stack()
    marked = {initial}
    s.push(initial)
    while s:
        parent = s.pop()
        if _test(parent):
            return parent
        children = _next(parent)
        for child in children:
            if child not in marked:
                marked.add(child)
                s.push(child)

class Cell(IntEnum):
    EMPTY = 255
    BLOCKED = 0
    START = 100
    END = 200
    PATH = 150

class MazeLocation(NamedTuple):
    row: int
    col: int

class Maze:
    def __init__(self, rows: int = 10, cols: int = 10,
                 sparse: float = 0.2, seed: int = 365,
                 start: MazeLocation = MazeLocation(0,0),
                 end: MazeLocation = MazeLocation(9,9), *,
                 grid: Optional[np.array] = None) -> None:
        np.random.seed(seed)
        self._start: MazeLocation = start
        self._end: MazeLocation = end
        self._grid: np.array = np.random.choice([Cell.BLOCKED, Cell.EMPTY],
                                                (rows, cols), p=[sparse, 1-sparse])
        self._grid[start] = Cell.START
        self._grid[end] = Cell.END

    class _Node:
        def __init__(self, state, parent):
            self.state = state
            self.parent = parent

    def _test_goal(self, ml: MazeLocation) -> bool:
        return ml == self._end
    
    def _success(self, ml: MazeLocation) -> List[MazeLocation]:
        location: List[MazeLocation] = []
        row, col = self._grid.shape
        if ml.row + 1 < row and self._grid[ml.row + 1, ml.col] != Cell.BLOCKED:
            location.append(MazeLocation(m1.row + 1, m1.col))
        if m1.row - 1 >= 0 and self._grid[m1.row - 1, m1.col] != Cell.BLOCKED:
            location.append(MazeLocation(m1.row - 1, m1.col))
        if m1.col + 1 < col and self._grid[ml.row, ml.col + 1] != Cell.BLOCKED:
            location.append(MazeLocation(ml.row, ml.col + 1))
        if ml.col - 1 >= 0 and self._grid[ml.row, ml.col - 1] != Cell.BLOCKED:
            location.append(MazeLocation(ml.row, ml.col -1))
        return location

class DepthFirstSearch(Maze):
    def _search(self):
        stack: Stack = Stack()
        initial: DepthFirstSearch._Node = self._Node(self._start, None)
        marked: Set[MazeLocation] = {initial.state}
        stack.push(initial)
        while stack:
            parent: DepthFirstSearch._Node = stack.pop()
            state: MazeLocation = parent.state
            if self._test_goal(state):
                return parent
            children: List[MazeLocation] = self._success(state)
            for child in children:
                if child not in marked:
                    marked.add(child)
                    stack.push(self._Node(child, parent))
    
    def show_path(self, pause: float = 0.5, *, plot: bool = True) -> Node:
        if pause <= 0:
            raise ValueError('pause must be more than 0')
        path: Maze._Node = self._search()
        if path is None:
            print('Path not found')
            return
        path = path.parent
        while path.parent is not None:
            self._grid[path.state] = Cell.PATH
            if plot:
                self._draw(pause)
            path = path.parent
        
        print('Path Done')
'''

from collections import deque   # linear table module

# define a graph class
class Graph(object):
    def __init__(self, *args, **kwargs):
        self.visited = []   # visited order
        self.neighbor = {}
    
    def add_node(self, node):
        key, val = node
        if not isinstance(val, list):
            raise ValueError('Input node should be a linear list')
        self.neighbor[key] = val
    
    def BFS(self, root):
        if root != None:
            search_queue = deque()
            search_queue.append(root)
            visited = []
        else:
            print('root is None')
            return -1
        
        while search_queue:
            person = search_queue.popleft()
            self.visited.append(person)

            if (not person in visited) and (person in self.neighbor.keys()):
                search_queue += self.neighbor[person]
                visited.append(person)
    
    def DFS(self, root):
        if root != None:
            search_queue = deque()
            search_queue.append(root)

            visited = []
        else:
            print('root is None')
            return -1
        
        while search_queue:
            person = search_queue.popleft()
            self.visited.append(person)

            if (not person in visited) and (person in self.neighbor.keys()):
                tmp = self.neighbor[person]
                tmp.reverse()

                for index in tmp:
                    search_queue.appendleft(index)
                
                visited.append(person)
    
    def clear(self):
        self.visited = []
    
    def node_print(self):
        for index in self.visited:
            print(index, end=' ')

if __name__ == '__main__':
    g = Graph()
    g.add_node(('A', ['B', 'C']))
    g.add_node(('B', ['D', 'E']))
    g.add_node(('C', ['F']))

    g.BFS('A')
    print('Breadth First Search: ')
    print(' ', end=' ')
    g.node_print()
    g.clear()

    print('\n\nDepth First Search: ')
    print(' ', end=' ')
    g.DFS('A')
    g.node_print()
    print()
