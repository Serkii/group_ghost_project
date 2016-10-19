from map import rooms
from player import *
from items import *
from gameparser import *
from sound import *
from ghosts import *
import random
import pickle
import sys
import time
from enum import Enum

class GameState(Enum):
    main = 0
    inventory = 1
    fight = 2
    dead = 3

SAVE_FILE = "save_data"

def converse(ghost):
	print("You approach %s." % ghost["name"])
	if "conversation" in ghost:
		do_response(ghost["conversation"])
	else:
		print("This ghost doesn't seem that interested in conversation")

def hurt_player():
	global sanity
	sanity -= 50
	return "test2"
	
def do_response(response):
	print(response["speech"])
	if "function" in response:
		resp = globals()[response["function"]]()
		if resp:
			do_response(response["responses"][resp])
			return
	if "responses" in response:
		user_resp = "";
		while True:
			print("\n".join([" - " + r for r in response["responses"].keys()]))
			user_resp = input("> ")
			if user_resp in response["responses"]:
				do_response(response["responses"][user_resp])
				return
			print("Could you repeat that? (Note: This part is case-sensitive because I'm lazy)")

def insert_name():
    print("")
    print("Welcome! Please enter your name: ")
    user_input = input()
    return user_input

def print_intro(name):
    text = """
You are """ + name + """, a Delivery Driver for Pizza Haunt, the number one Pizza company in the whole town,
also the only Pizza Company in the whole town but minor details are irrelevant.
You and your trusty scooter had been all across town delivery all sorts of pizza's with all sorts of toppings and your shift was almost up when you receive one last order...

2 Margarita Pizza's
1 Hawaiian Pizza
Garlic Bread

It would normally be a simple task for once such as yourself but the address puzzles both you and your co-workers,
the address is that of Clearview Mansion, a run-down house that hasn't seen use in over a hundred years.
Still your company has a delivery in 30 minutes guarantee and since the order has already been paid for you better make your way over there.

Also there was an odd note included with the order: 'Send help, ghosts about'

""".format(name)

    #for char in text:
        #time.sleep(0.01)
        #print(char, end="")
        #sys.stdout.flush()

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
    print("Your sanity is at " + str(sanity) + "%.")
    print("")
    print("You can:")
    print("Type INV to access inventory menu and player status.")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    for item in room_items:
        print("TAKE " + str.upper(item["id"]) + " to take " + item["name"] + ".")
    for item in room_items:
        print("EXAMINE " + str.upper(item["id"]) + " to get more information about this item.")
    
    print("Type SAVE to save the game.")
    print("What do you want to do?")

def print_inv_menu(inventory):

    print("Your sanity is at " + str(sanity) + "%.")
    print("")
    print("You can:")

    for item in inventory:
        print("EXAMINE " + str.upper(item["id"]) + " to get more information about this item.")
    for item in inventory:
        print("DROP " + str.upper(item["id"]) + " to drop " + item["name"] + ".")
    print("EXIT this menu.")
    print("What do you want to do?")

def print_combat_menu(inventory, ghost):
    print("")
    print(ghost["name"] + " has " + str(ghost["hp"]) + " health.")
    print("Your sanity is at " + str(sanity) + "%.")
    print("")
    print("You can: ")
    print("FIGHT to attack the ghost with your weapon.")
    print("EXAMINE to look at the ghost more closely.")
    for item in inventory:
        print("USE " + str.upper(item["id"]) + " to try and use " + item["name"] + ".")
    print("TALK to try and speak to the ghost.")
    print("RUN to attempt escape!")
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

    global gamestate

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
        if current_room["ghost_in_room"]:
            print("You cannot save here! There are ghosts nearby.")
        else:
            save_state()
            print("Saving progress...")

    elif command[0] == "load":
        load_state()
        print("Loading saves...")

    elif command[0] == "examine":
        if gamestate == GameState.main:
            execute_examine_room(command[1])
        elif gamestate == GameState.inventory:
            execute_examine_inv(command[1])


    elif command[0] == "inv":
        gamestate = GameState.inventory

    elif command[0] == "exit":
        if gamestate == GameState.inventory:
            gamestate = GameState.main
            main()



    else:
        print("This makes no sense.")

def execute_combat_command(command, ghost, inventory, room):

    global sanity
    global gamestate


    if 0 == len(command):
         return

    if command[0] == "fight":
        if item_proton_gun in inventory:
            player_combat_skill = 7
            player_attack_power = player_combat_skill + random.randrange(1, 13)
            player_attack_power *= attack_multiplier
            ghost_attack_power = ghost["combat_skill"] + random.randrange(1, 13)
            if player_attack_power > ghost_attack_power:
                print(ghost["damage_text"])
                ghost["hp"] -= 10 * attack_multiplier
            elif ghost_attack_power > player_attack_power:
                print(ghost["onhit_text"])
                sanity -= 10 * defense_multiplier
            elif player_attack_power == ghost_attack_power:
                print(ghost["name"] + " avoids the attack!")
        else:
            print("You have no weapon that can harm a ghost!")
            print(ghost["onhit_text"])
            sanity -= 10 * defense_multiplier

    elif command[0] == "examine":
        print(ghost["desc"])

    elif command[0] == "use":
        print("PLACEHOLDER")

    elif command[0] == "talk":
        converse(ghost)

    elif command[0] == "run":
        player_escape = random.randrange(1, 13) * attack_multiplier
        ghost_catch = random.randrange(1, 13)
        if ghost_catch > player_escape:
            print("You failed to escape!")
            print(ghost["onhit_text"])
            sanity -= 10 * defense_multiplier
        elif player_escape >= ghost_catch:
            print("You escape, but which way?")
            for direction in current_room["exits"]:
                # Print the exit name and where it leads to
                print_exit(direction, exit_leads_to(current_room["exits"], direction))
                
            user_input = input("> ")
            normalised_user_input = normalise_input(user_input)
            if len(normalised_user_input) > 1:
                execute_go(normalised_user_input[1])
                gamestate = GameState.main
                main()
            else:
                print("You can't do that.")









def execute_approach(npc_name):
    global current_room
    npc_matches = [npc for npc in current_room.get("npcs", []) if npc["name"].lower() == npc_name]
    if npc_matches:
        converse(npc_matches[0])
    else:
        print("I can't see %s here..." % npc_name)

def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """

    global current_room
    global gamestate
    if is_valid_exit(current_room["exits"], direction) == True:
        new_room = move(current_room["exits"], direction)
        if "on_enter" in new_room and not new_room["on_enter"](new_room):
            return
        current_room = new_room
        if current_room["ghost_in_room"] == True:
            print("")
            print(current_room["condition"])
            print("")
            gamestate = GameState.fight

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
        calculate_stats()
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
        calculate_stats()
    else:
        print("You cannot drop that.")


def execute_examine_room(item_id):

    item_matches = [item for item in current_room["items"] + inventory if item["id"] == item_id]
    if item_matches:
        print(item_matches[0]["desc"])
    else:
        print("You cannot examine that.")

def execute_examine_inv(item_id):

    global inventory

    item_matches = [item for item in inventory if item["id"] == item_id]
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

def inv_menu(inventory):

    print_inv_menu(inventory)

    user_input = input("> ")

    normalised_user_input = normalise_input(user_input)

    return normalised_user_input

def combat_menu(inventory, ghost, room):

    global sanity
    global gamestate
    global first_turn

    if sanity > 0:
        if ghost["hp"] > 0:

            if first_turn == True:
                enter_combat(ghost)
                first_turn = False


            print_combat_menu(inventory, ghost)

            user_input = input("> ")

            normalised_user_input = normalise_input(user_input)

            return normalised_user_input

        else:
            print(ghost["death_text"])
            room["ghost_in_room"] = False
            gamestate = GameState.main
            main()
    else:
        gamestate = GameState.dead
        main()


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

def enter_combat(ghost):

    print(ghost["name"] + " approaches!")
    if ghost["player_escaped"] == False:
        print(ghost["intro"])
    elif ghost["player_escaped"] == True:
        print(ghost["intro2"])

def save_state():
    global sanity
    state = [current_room, rooms, sanity]
    save_file = open(SAVE_FILE, "wb")
    pickle.dump(state, save_file)
    save_file.close()

def load_state():
    global current_room
    global sanity
    global rooms
    global gamestate
    save_file = open(SAVE_FILE, "rb")
    state = pickle.load(save_file)
    save_file.close()
    rooms = state[1]
    current_room = state[0]
    sanity = state[2]
    calculate_stats()
    gamestate = GameState.main

    # This is the entry point of our program
def main():

    #print_intro("PLACEHOLDER NAME")
    # Main game loop
    while gamestate == GameState.main:

    
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)

    while gamestate == GameState.inventory:

        print("")
        print_inventory_items(inventory)

        command = inv_menu(inventory)

        execute_command(command)

    while gamestate == GameState.fight:

        current_ghost = current_room["ghost"]

        command = combat_menu(inventory, current_ghost, current_room)

        execute_combat_command(command, current_ghost, inventory, current_room)

    while gamestate == GameState.dead:
        print("""
            # #  #  # #      #  ##  ###     ##  ###  #  ##              
### ###     # # # # # #     # # # # #       # # #   # # # #     ### ### 
             #  # # # #     ### ##  ##      # # ##  ### # #             
### ###      #  # # # #     # # # # #       # # #   # # # #     ### ### 
             #   #  ###     # # # # ###     ##  ### # # ##             
        """)
        print("Maybe you should be more careful next time.")
        print("Do you want to play from your last save? Y/N")
        replay = input("> ")
        if replay[0].upper() == "Y":
            load_state()
            print("Loading last save...")
            main()
        else:
            print("""                                                            
             ##  #  # # ###      #  # # ### ##              
### ###     #   # # ### #       # # # # #   # #     ### ### 
            # # ### ### ##      # # # # ##  ##              
### ###     # # # # # # #       # # # # #   # #     ### ### 
             ## # # # # ###      #   #  ### # #            
             """)
        break


        
        



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    load_sounds()
    player_name = insert_name()
    print_intro(player_name)
    gamestate = GameState.main
    save_state()
    first_turn = True
    main()
