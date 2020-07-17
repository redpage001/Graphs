from room import Room
from player import Player
from world import World
from util import Stack, Queue, Graph

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def traverse():
    graph = Graph()
    visited = set()
    test_path = list()
    mapped_rooms = graph.dft(player.current_room) # maps out the graph connecting each room with its neighbors
    rooms = [room for room in mapped_rooms] # a list of all rooms in the order in which they were added to the stack

    while len(visited) < len(room_graph) - 1:
        path = graph.bfs(rooms[0], rooms[1]) # As long as there's rooms to visit, we take the shortest path between the first two rooms

        while len(path) > 1: # While there is at least two rooms in the shortest path we check if the adjacent_room is a neighbor of the current_room and if it is we append the direction value to the adjacent_room
            current_room = path[0]
            adjacent_room = path[1]
            
            if adjacent_room in mapped_rooms[current_room]:
                test_path.append(mapped_rooms[current_room][adjacent_room])
            path.remove(current_room)
        rooms.remove(rooms[0]) # Removes the room you checked and ads it to the visited so that you can keep checking each room through the list
        visited.add(rooms[0])

    return test_path

def repeat():
    global traversal_path
    traversal_path = traverse()
    print(f"TESTS PASSED: {len(traversal_path)} moves")

    old_length = len(traversal_path)

    while len(traversal_path) > 950:
        traversal_path = traverse()
        if len(traversal_path) < old_length:
            print(f"TESTS PASSED: {len(traversal_path)} moves")
            old_length = len(traversal_path)

repeat()

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")