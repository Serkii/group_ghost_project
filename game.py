from map import rooms
from player import *
from items import *
from gameparser import *
from sound import *
import pickle


SAVE_FILE = "save_data"

def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_camera, item_pizza])
    'a rusty, antique camera, the pizza'

    >>> list_of_items([item_pizza])
    'the pizza'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_camera, item_pizza, item_proton_gun])
    'a rusty, antique camera, the pizza, a proton gun'

    """
    item_list = ""
    for dictionary in items:
        if item_list == "":
            item_list = item_list + dictionary["name"]
        else:
            item_list = item_list + ", " + dictionary["name"]
    return item_list


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

   -------- TEST TO BE ADDED AFTER ITEM LOCATIONS DETERMINED ----------

   also, I changed the wording a little to reflect that other items may be in the room
   but not visible yet - Rowan



    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    if not (room["items"] == []):
        print("""You can see """ + list_of_items(room["items"]) + """ here.
        """)

def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

	this test might need updating if the player has other starting items

    >>> print_inventory_items(inventory)
    You have the pizza.
    <BLANKLINE>

    """
    print("You have " + list_of_items(items) + """.
        """)

def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    ------ TESTS TO BE ADDED AFTER ROOM STARTING STATES DETERMINED ------


    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    print_room_items(room)
    

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    ------ TESTS TO BE ADDED LATER ------


    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    ------- TESTS TO BE ADDED LATER ------
    also we'll need to decide if we want compass directions or more descriptive methods? - Rowan

    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    EXAMINE BISCUITS to get more information about this item.
    EXAMINE HANDBOOK to get more information about this item.
    EXAMINE ID to get more information about this item.
    EXAMINE LAPTOP to get more information about this item.
    EXAMINE MONEY to get more information about this item.
    What do you want to do?

    """
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    for item in room_items:
        print("TAKE " + str.upper(item["id"]) + " to take " + item["name"] + ".")
    for item in inv_items:
        print("DROP " + str.upper(item["id"]) + " to drop " + item["name"] + ".")
    for item in room_items:
        print("EXAMINE " + str.upper(item["id"]) + " to get more information about this item.")
    for item in inv_items:
        print("EXAMINE " + str.upper(item["id"]) + " to get more information about this item.")
    
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

	------ TESTS TO BE ADDED LATER ------

    """
    return chosen_exit in exits

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")
            
    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "save":
        save_state()

    elif command[0] == "load":
        load_state()

    elif command[0] == "examine":
        execute_examine(command[1])

    else:
        print("This makes no sense.")

def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """

    global current_room
    if is_valid_exit(current_room["exits"], direction) == True:
        current_room = move(current_room["exits"], direction)
    else:
        print("You cannot go that way.")

def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    item_matches = [item for item in current_room["items"] if item["id"] == item_id]
    if item_matches:
        current_room["items"].remove(item_matches[0])
        inventory.append(item_matches[0])
    else:
        print("You cannot take that.")
    

def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    item_matches = [item for item in inventory if item["id"] == item_id]
    if item_matches:
        inventory.remove(item_matches[0])
        current_room["items"].append(item_matches[0])
    else:
        print("You cannot drop that.")


def execute_examine(item_id):

    item_matches = [item for item in current_room["items"] + inventory if item["id"] == item_id]
    if item_matches:
        print(item_matches[0]["desc"])
    else:
        print("You cannot examine that.")
        
def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input

def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    play_sound("door_open.wav")
    return rooms[exits[direction]]

def save_state():
    state = [current_room, rooms]
    save_file = open(SAVE_FILE, "wb")
    pickle.dump(state, save_file)
    save_file.close()

def load_state():
    global current_room
    save_file = open(SAVE_FILE, "rb")
    state = pickle.load(save_file)
    save_file.close()
    rooms = state[1]
    current_room = state[0]

    # This is the entry point of our program
def main():

    load_sounds()
    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
