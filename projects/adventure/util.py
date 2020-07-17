import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
    
class Graph:
    def __init__(self):
        self.vertices = {}

    def dft(self, starting_vertex):
        s = Stack()
        visited = set()
        s.push([starting_vertex])

        while s.size() > 0:
            path = s.pop()
            last_room = path[-1]

            if last_room not in visited:
                visited.add(last_room)
                self.vertices[last_room.id] = {}
                exits = last_room.get_exits()
                
                for direction in exits:
                    adjacent_room = last_room.get_room_in_direction(direction)
                    self.vertices[last_room.id][adjacent_room.id] = direction

                while len(exits) > 0:
                    random_exit = random.randrange(0, len(exits))
                    direction = exits[random_exit]
                    copy_path = path.copy()
                    copy_path.append(last_room.get_room_in_direction(direction))
                    s.push(copy_path)
                    exits.remove(direction)
        
        return self.vertices

    def bfs(self, starting_vertex, destination_vertex):
        q = Queue()
        visited = set()
        q.enqueue([starting_vertex])

        while q.size() > 0:
            path = q.dequeue()
            last_room = path[-1]

            if last_room == destination_vertex:
                return path
            if last_room not in visited:
                visited.add(last_room)

                for neighbor in self.vertices[last_room]:
                    copy_path = path.copy()
                    copy_path.append(neighbor)
                    q.enqueue(copy_path)