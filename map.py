from items import *
#from npc import *

def lobby_on_enter(lobby):
    lobby.pop("on_enter", None)
    # *play sound*
    print("The front door slams shut behind you!")

room_outside = {
    "name": "Outside",
    "description": """DESCRIPTION""",
    "exits": {"north": "RoomLobby"},
    "items": []
}

room_lobby = {
    "name": "Lobby",
    "description": """DESCRIPTION""",
    "exits": {"upstairs": "RoomLandingCentre", "east": "RoomLiving", "west": "RoomDining"},
    "on_enter": lobby_on_enter,
    "items": [item_proton_gun]
}

room_living = {
    "name": "Living Room",
    "description": """DESCRIPTION""",
    "exits": {"west": "RoomLobby"},
    "items": []
}

room_dining = {
    "name": "Dining Room",
    "description": """DESCRIPTION""",
    "exits": {"north": "RoomKitchen", "east": "RoomLobby"},
    "items": []
}

room_kitchen = {
    "name": "Kitchen",
    "description": """DESCRIPTION""",
    "exits": {"south": "RoomDining"},
    "items": []
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
    "items": []
}

room_landing_left = {
    "name": "The Left of the Landing",
    "description": """A gigantic stain glass window at the end of the hall sends an array of red and blue light into the miserable indoors.
The door to the storage room in front of you has a beaten down, rusty lock hanging from the handle.
The children’s room is opposite and a slight pink glow radiates from the inside.
The atmosphere feels very sombre and gloomy.""",
    "exits": {"east": "RoomLandingCentre", "north": "RoomStorage", "south": "RoomChildBedroom"},
    "items": []
}

room_landing_right = {
    "name": "The Right of the Landing",
    "description": """This side of the floor has definitely taken a toll throughout the years.
cobwebs clothe the ceiling and the red carpet that was once a luxurious,soft possession is now a tragic entity.
you are standing by the bathroom, a place that seems perfect for wicked dead souls to reside in.
There is a strange, medieval painting on the wall opposite to the bathroom, bigger than the rest.
It’s captivating and almost inviting you to step in, breaking the barrier between the past and the present.""",
    "exits": {"west": "RoomLandingCentre", "north": "RoomBathroom", "south": "RoomHidden"},
    "items": []
}

room_master_bedroom = {
    "name": "Master Bedroom",
    "description": """You are now in the vast and impressive master bedroom.
An intricately designed domed ceiling is now falling down pieces by pieces.
The large windows next to the magnificent four poster bed overlook the overgrown mazes in the acres of land that connect to the woods.
An aged chest lies at the foot of the bed wrapped around tightly in untouched chains clamped with an ancient lock.
In the corner of the room is a dressing table with a dust-covered mirror and broken chair.""",
    "exits": {"south": "RoomLandingCentre", "east": "RoomBathroom"},
    "items": []
}

room_library = {
    "name": "Library",
    "description": """You are now in the library.
Tall, dark bookshelves line the entirety of the room.
Most of the ancient books are fallen, lying on the ground in a chaotic state making the shelves look sparse.
An armchair ripped to shreds and a coffee table, with one leg short are situated in the middle of the room.
You are surrounded by information that could be helpful to complete your mission.
""",
    "exits": {"south": "RoomLandingLeft"},
    "items": []
}

room_child_bedroom = {
    "name": "Child's Bedroom",
    "description": """You are now in the children’s room.
Soft, peaceful music plays from a music box on a bookshelf.
A headless ballerina spins in the box.
A rocking chair and wooden chair sway to the melody.
The big window is plastered off but a pink aura is present in the room illuminating the space.
""",
    "exits": {"north": "RoomLandingLeft"},
    "items": []
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
    "items": []
}

room_hidden = {
    "name": "Hidden Room",
    "description": """You are now in the hidden room!!
Right in front of you is the Ghost-Busters team tied to each other back-to-back.
Free them so that they enjoy their pizza and you can get your tip!""",
    "exits": {"north": "RoomLandingRight"},
    "items": []
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
    "RoomStorage": room_library,
    "RoomChildBedroom": room_child_bedroom,
    "RoomBathroom": room_bathroom,
    "RoomHidden": room_hidden
}
