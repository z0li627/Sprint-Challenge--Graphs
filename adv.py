from room import Room
from player import Player
from world import World

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

# Fill this out with dirs to walk
# traversal_path = ['n', 'n']
traversal_path = []
croom = world.rooms[0]
visited = set()
tmp = []

while len(visited) < len(world.rooms):
    dirs = []
    visited.add(croom.id)
    if croom.w_to != None and croom.w_to.id not in visited:
        dirs.append("w")
    if croom.n_to != None and croom.n_to.id not in visited:
        dirs.append("n")
    if croom.e_to != None and croom.e_to.id not in visited:
        dirs.append("e")
    if croom.s_to != None and croom.s_to.id not in visited:
        dirs.append("s")
    if len(dirs) > 0:
        move = random.choice(dirs)
        traversal_path.append(move)
        tmp.append(move)
        if move == "n":
            croom = croom.n_to
        if move == "s":
            croom = croom.s_to
        if move == "e":
            croom = croom.e_to
        if move == "w":
            croom = croom.w_to
    if len(dirs) == 0:
        last_move = tmp.pop()
        if last_move == "w":
            croom = croom.e_to
            traversal_path.append("e")
        if last_move == "n":
            croom = croom.s_to
            traversal_path.append("s")
        if last_move == "e":
            croom = croom.w_to
            traversal_path.append("w")
        if last_move == "s":
            croom = croom.n_to
            traversal_path.append("n")

# TRAVERSAL TEST - DO NOT MODIFY
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
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
