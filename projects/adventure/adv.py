from room import Room
from player import Player
from world import World
from utils import Stack, Queue  # These may come in handy


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
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
graphCache = {}


def bfs_populate_map(starting_room_id):
    q = Queue()
    q.enqueue([starting_room_id])
    visited = set()

    while q.size() > 0:

        # removing first ath
        p = q.dequeue()
        current_room = p[-1]

    # add current location to visited
        visited.add(current_room)

    # if current_room not in visited:
    #     if vertex
        for direction in graphCache[current_room]:
            if graphCache[current_room][direction] is "?":
                return p
            if graphCache[current_room][direction] not in visited:
                new_path = list(p)  # copy path
            # append the list to the back
                new_path.append(graphCache[current_room][direction])
                q.enqueue(new_path)


def dft_search(starting_room):
    opp_dirctions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
    rooms = 0

    while len(graphCache) != len(room_graph):
        current_room = player.current_room
        room_id = current_room.id

        # add full data into the room
        room_data = {}

        if room_id not in graphCache:
            for id in current_room.get_exits():
                room_data[id] = "?"

            # update room
            if traversal_path:
                room_previous = opp_dirctions[traversal_path[-1]]
                room_data[room_previous] = rooms

            graphCache[room_id] = room_data

        else:
            room_data = graphCache[room_id]

        possible_exits = list()

        for direction in room_data:
            if room_data[direction] == "?":
                possible_exits.append(direction)

        if len(possible_exits) != 0:
            random.shuffle(possible_exits)

            direction = possible_exits[0]

            traversal_path.append(direction)

            player.travel(direction)

            room_move = player.current_room

            graphCache[current_room.id][direction] = room_data.id

        else:
            next_room = bfs_populate_map(room_id)

            if next_room is not None and len(next_room) > 0:
                for i in range(len(next_room)-1):
                    for direction in graphCache[next_room[i]]:
                        if graphCache[next_room[i][direction] == next_room[i+1]]:
                            traversal_path.append(direction)
                            player.travel(direction)
        # else:
        #     break


dft_search(room_graph)
print('graph cache-->', graphCache)
print('traversal ', traversal_path)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print("hello")
    # print(
    #     f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    # print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")
    print('hello thee')

######
# UNCOMMENT TO WALK AROUND
######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
