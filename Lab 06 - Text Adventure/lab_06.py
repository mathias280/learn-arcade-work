class Room:
    def __init__(self, north, south, east, west):
        self.description = ""
        self.north = 0
        self.south = 0
        self.east = 0
        self.west = 0


def main():

    done = False

    # Current Room
    room = 0

    # The Room List
    room_list = []

    # Defined Rooms
    # Start, Kitchen - Room 0
    room = Room("You have awoken in a kitchen from sleep walking. You see a door to your east and the south.", None, 1, 2,
            None)
    room_list.append(room)

    # Hall - Room 1
    room = ("You have opened the door and entered into a hall. There is a single door to the south.", None, None, 3,
            None)
    room_list.append(room)

    # Bathroom - Room 2
    room = ("You open the door and find yourself in a large bathroom. There is one door to the east.", None, 3, None,
            None)
    room_list.append(room)

    # Living room - Room 3
    room = ("You enter through the door and find yourself in a large living room. There are doors to the north, west, "
            "and stairs to the east.", 1, 4, None, 2)
    room_list.append(room)

    # Basement - Room 4
    room = ("You have went down two flights of stair and find your in near darkness at the bottom. There appears to "
            "be a "
            "hole in the wall to the east.", None, 5, None, None)
    room_list.append(room)

    # Cave - Room 5
    room = ("You crawl through the hole and find yourself in what appears to be a man-made cave. There is a light "
            "above a "
            "door to the south.", None, None, 6, None)
    room_list.append(room)

    # empty room - Room 6
    room = ("You open the door to what appears to be an empty storage room. Though you look closer and see a trap "
            "door in "
            "the west corner.", None, None, None, 7)
    room_list.append(room)
    current_room = 0

    # While loop
    while not done:

        next_room = current_room
        # Room List
        print(room_list[current_room][0])
        print()
        # input
        user_input = input("Where would you like to go? Quit game by typing Q or Quit!")

        # IF - North
        if user_input.lower() == "n" or user_input.lower() == "north":
            next_room = room_list[current_room][1]
        elif next_room is None:
            print("There is nothing that way!")

        # IF - East
        if user_input.lower() == "e" or user_input.lower() == "east":
            next_room = room_list[current_room][2]
        elif next_room is None:
            print("There is nothing that way!")


        # IF - South
        if user_input.lower() == "s" or user_input.lower() == "south":
            next_room = room_list[current_room][3]
        elif next_room is None:
            print("There is nothing that way!")


        # IF - West
        if user_input.lower() == "w" or user_input.lower() == "west":
            next_room = room_list[current_room][4]
        elif next_room is None:
            print("There is nothing that way!")


        # IF - Quit
        if user_input.lower() == "q" or user_input.lower() == "quit":
            done = True
            print("Thank you for playing! Hope you had fun!")
        current_room = next_room

        if current_room == 7:
            done = True
            print("You have escaped!")
            print()
            print("Thank you for playing! Hope you had fun!")

main()
