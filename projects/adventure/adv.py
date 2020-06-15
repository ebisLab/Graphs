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


def dfs_search(starting_room):
    # opp_dirctions = {}
    # opp_dirctions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
    opp_dirctions = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

    count = 0  # initial value to room couner

    while len(graphCache) != len(room_graph):
        current_room = player.current_room
        room_id = current_room.id

        # add full data into the room
        room_data = {}
        exit_room = list()
        if room_id not in graphCache:
            for id in current_room.get_exits():
                room_data[id] = "?"

            graphCache[room_id] = room_data

            # update room
            if traversal_path:
                room_previous = opp_dirctions[traversal_path[-1]]
                # add that to the room counter
                room_data[room_previous] = count

        else:
            room_data = graphCache[room_id]

        for direction in room_data:
            if room_data[direction] == "?":
                exit_room.append(direction)

        if len(exit_room) is not 0:
            random.shuffle(exit_room)
            # set the direction to the possible exits in the first positon

            direction = exit_room[0]

            traversal_path.append(direction)
            # part that player moves
            player.travel(direction)
            room_move = player.current_room
            graphCache[current_room.id][direction] = room_move.id

        else:
            # search by room id
            next_room = bfs_populate_map(room_id)

            if next_room is not None and len(next_room) > 0:
                # loop room to gain access to the room's id
                for i in range(len(next_room)-1):
                    # loop to access direction
                    for direction in graphCache[next_room[i]]:
                        if graphCache[next_room[i]][direction] == next_room[i+1]:
                            traversal_path.append(direction)
                            player.travel(direction)  # player is moving
            # else:
            #     break


dfs_search(room_graph)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#####
# UNCOMMENT TO WALK AROUND
#####
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
