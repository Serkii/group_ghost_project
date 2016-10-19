from items import *
from ghosts import *

#Added some conditions that need to be implemented into the code

room_outside = {
    "name": "Outside",
    "description": """You stand on a hill overlooking the whole town, in front of you stands 
Clearview Mansion, it looks as if it was made by an Architect checking off
boxes on 'Gothic Revival Clichés' but you can't help but imagine how grand
this place must have been in its prime, instead it has seen nothing but neglect,
most windows have shattered, the roof has practically collapsed in on itself and
it's hard to make out the original colour of the walls what with all the graffiti
applied to it. Your moped purrs' and waits on standby for your return, once the 
pizzas have been delivered of course.""",
    #condition: You should not be able to return to this room once entering the lobby
    "exits": {"inside": "RoomLobby"},
    "items": [],
    "ghost": "",
    "ghost_in_room": False
}

room_lobby = {
    "name": "Lobby",
    "description": """You are currently standing in the Lobby, the remains of the chandelier litter the
centre of the room, many tiles have fallen from the ceiling and the rotting floorboards
make it dangerous to navigate safely. Rays of light enter the room from the broken windows
at the front of the house. One ray illuminates a small bust situated underneath the balcony
of the second floor.""",
    #condition: "A strong ghostly aura blocks you from climbing the stairs"
    "exits": {"upstairs": "RoomLandingCentre", "east": "RoomLiving", "west": "RoomDining"},
    "on_enter": "lobby_on_enter",
    "items": [item_proton_gun, item_walkie_talkie],
    "ghost_in_room": False,
    "ghost": ""
}

room_living = {
    "name": "Living Room",

    "description": """Entering the Living room was easy, the doors have rotted so greatly that they 
have fallen from their hinges. Despite the Mansion giving off an unnerving atmosphere
the living room proves oddly serene. The windows that reveal the east garden somehow
remain untouched by the decay found throughout the rest of the house. You hear a soft
classical melody originating from a gramophone in the corner of the room, 
the melody is paired with the soft crackle of the fireplace attached to the north wall.
Somehow the fire still burns.""",

    #the condition below is for test_ghost, can be removed to use above ghost condition later
    "condition": "In front of the fire a Doberman rests, when you try to focus your eyes on him he seemingly disappears.",
    "exits": {"west": "RoomLobby"},
    "items": [item_firepoker],
    "ghost": ghost_dog,
    "ghost_in_room": True
}

room_dining = {
    "name": "Dining Room",
    "description": """You stand now in the Dining Room, the wallpaper has peeled off in most places and only
a few candle holders are still attached to the walls. To your left you see the broken windows
that reveal the front of the house and your moped that helped you get here. The dining table
covers most of the room and can fit ten people. Smashed cutlery litters the table.""",

    "condition": """A ghostly figure sits at the head of the table, he seems to be eating something but there is nothing on his plate
    Something tells you that you won't be getting into the kitchen until this man has been dealt with.""",

    "exits": {"north": "RoomKitchen", "east": "RoomLobby"},
    "items": [item_platter],
    "ghost": ghost_Pinkerton,
    "ghost_in_room": True
}

room_kitchen = {
    "name": "Kitchen",
    "description": """You are now in the Kitchen, encompassing the walls are various ruined cabinets each storing some
form of crockery most of which is ruined beyond repair. You know not how old this mansion is but you
are certain that the refrigerator is a new addition, it has a metallic sheen to it, uncharacteristic
of the rest of the house. There is a weird small of gas in the room and you feel it would be a bad idea
to turn on a light switch... that would be if the mansion had working electricity in the first place.""",

    "condition": "A ghostly figure faces a counter and hacks away at a pig carcass.",
    "exits": {"south": "RoomDining"},
    "items": [item_ham],
    "ghost": ghost_Chef,
    "ghost_in_room": True
}

room_landing_centre = {
    "name": "The Middle of the Landing",
    "description": """You have now entered the first floor.
The air is stuffy and is embedded with a pungent, musky scent.
Pictures, dead lanterns and fractured mirrors line the cracked and peeling walls.
To your tight, a dim lighted lantern hangs.
A sign of life in this arid dwelling?
A large, grande, wooden door centres the landing leading to the master bedroom, where the most affluent used to slumber.""",
    "exits": {"downstairs": "RoomLobby", "north": "RoomMasterBedroom", "east": "RoomLandingRight", "west": "RoomLandingLeft"},
    "items": [],
    "ghost_in_room": False,
    "on_enter": "stairs_permission_check",
    "ghost": ""
}

room_landing_left = {
    "name": "The Left of the Landing",
    "description": """A gigantic stain glass window at the end of the hall sends an array of red and blue light into the miserable indoors.
The door to the Library in front of you has a beaten down, rusty lock hanging from the handle.
The children's room is opposite and a slight pink glow radiates from the inside.
The atmosphere feels very sombre and gloomy.""",
    "exits": {"east": "RoomLandingCentre", "north": "RoomLibrary", "south": "RoomChildBedroom"},
    "items": [],
    "ghost_in_room": False,
    "ghost": "",
    "on_enter": "stop_close_music",
}

room_landing_right = {
    "name": "The Right of the Landing",
    "description": """This side of the floor has definitely taken a toll throughout the years.
cobwebs clothe the ceiling and the red carpet that was once a luxurious,soft possession is now a tragic entity.
you are standing by the bathroom, a place that seems perfect for wicked dead souls to reside in.
There is a strange, medieval painting on the wall opposite to the bathroom, bigger than the rest.
It's captivating and almost inviting you to step in, breaking the barrier between the past and the present.""",
    "exits": {"west": "RoomLandingCentre", "north": "RoomBathroom", "south": "RoomHidden"},
    "items": [],
    "ghost_in_room": False,
    "ghost": ""
}

room_master_bedroom = {
    "name": "Master Bedroom",
    "description": """You are now in the vast and impressive master bedroom.
An intricately designed domed ceiling is now falling down pieces by pieces.
The large windows next to the magnificent four poster bed overlook the overgrown mazes in the acres of land that connect to the woods.
An aged chest lies at the foot of the bed wrapped around tightly in untouched chains clamped with an ancient lock.
In the corner of the room is a dressing table with a dust-covered mirror and broken chair.""",
    "condition": "<Ghost here>",
    "exits": {"south": "RoomLandingCentre", "east": "RoomBathroom"},
    "items": [],
    "ghost": ghost_Lady,
    "ghost_in_room": True
}

room_library = {
    "name": "Library",
    "description": """You are now in the library.
Tall, dark bookshelves line the entirety of the room.
Most of the ancient books are fallen, lying on the ground in a chaotic state making the shelves look sparse.
An armchair ripped to shreds and a coffee table, with one leg short are situated in the middle of the room.
You are surrounded by information that may be helpful to complete your mission.
""",
    "condition": "<Ghost here>",
    "exits": {"south": "RoomLandingLeft"},
    "items": [item_familytree, item_childsbook, item_ghostbook],
    "ghost": ghost_Poltergeist,
    "ghost_in_room": True
}

room_child_bedroom = {
    "name": "Child's Bedroom",
    "description": """You are now in the children's room.
Soft, peaceful music plays from a music box on a bookshelf.
A headless ballerina spins in the box.
A rocking chair and wooden chair sway to the melody.
The big window is plastered off but a pink aura is present in the room illuminating the space.
""",
    "condition": "<Ghost here>",
    "exits": {"north": "RoomLandingLeft"},
    "items": [],
    "ghost": ghost_toys,
    "ghost_in_room": True,
    "on_enter": "play_close_music",
}

room_bathroom = {
    "name": "Bathroom",
    "description": """You are in a very old, disgusting bathroom.
The presence of a damaged soul can be sensed.
The floor is scattered with old bottles, tubes and containers.
The bath tub is filled with a suspicious, unfamiliar blue viscous substance.
The sound of the dripping tap breaks the silence in the choking and claustrophobic air.
""",
    "exits": {"south": "RoomLandingRight", "west": "RoomMasterBedroom"},
    "items": [],
    "ghost_in_room": False,
    "ghost": ""
}

room_hidden = {
    "name": "Hidden Room",
    "description": """You are now in the hidden room!!
Right in front of you is the Ghost-Busters team tied to each other back-to-back.
Free them so that they enjoy their pizza and you can get your tip!""",
    "condition": "<Ghost here>",
    "exits": {"north": "RoomLandingRight"},
    "items": [],
    "ghost": ghost_julia,
    "ghost_in_room": True
}

rooms = {
    "RoomOutside": room_outside,
    "RoomLobby": room_lobby,
    "RoomLiving": room_living,
    "RoomDining": room_dining,
    "RoomKitchen": room_kitchen,
    "RoomLandingCentre": room_landing_centre,
    "RoomLandingLeft": room_landing_left,
    "RoomLandingRight": room_landing_right,
    "RoomMasterBedroom": room_master_bedroom,
    "RoomLibrary": room_library,
    "RoomChildBedroom": room_child_bedroom,
    "RoomBathroom": room_bathroom,
    "RoomHidden": room_hidden
}
