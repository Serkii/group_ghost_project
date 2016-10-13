from items import *
from npc import *

def lobby_on_enter(lobby):
    lobby.pop("on_enter", None)
    # *play sound*
    print("The front door slams shut behind you!")

room_outside = {
    "name": "Outside",
    "description": """DESCRIPTION""",
    "exits": {"north": "RoomLobby"}
}

room_lobby = {
    "name": "Lobby",
    "description": """DESCRIPTION""",
    "exits": {"upstairs": "RoomLandingCentre", "east": "RoomLiving", "west": "RoomDining"},
    "on_enter": lobby_on_enter
}

room_living = {
    "name": "Living Room",
    "description": """DESCRIPTION""",
    "exits": {"west": "RoomLobby"}
}

room_dining = {
    "name": "Dining Room",
    "description": """DESCRIPTION""",
    "exits": {"north": "RoomKitchen", "east": "RoomLobby"},
}

room_kitchen = {
    "name": "Kitchen",
    "description": """DESCRIPTION""",
    "exits": {"south": "RoomDining"}
}

room_landing_centre = {
    "name": "The Middle of the Landing",
    "description": """DESCRIPTION""",
    "exits": {"downstairs": "RoomLobby", "north": "RoomMasterBedroom", "east": "RoomLandingRight", "west": "RoomLandingLeft"}
}

room_landing_left = {
    "name": "The Left of the Landing",
    "description": """DESCRIPTION""",
    "exits": {"east": "RoomLandingCentre", "north": "RoomStorage", "south": "RoomChildBedroom"}
}

room_landing_right = {
    "name": "The Right of the Landing",
    "description": """DESCRIPTION""",
    "exits": {"west": "RoomLandingCentre", "north": "RoomBathroom", "south": "RoomHidden"}
}

room_master_bedroom = {
    "name": "Master Bedroom",
    "description": """DESCRIPTION""",
    "exits": {"south": "RoomLandingCentre", "east": "RoomBathroom"}
}

room_storage = {
    "name": "Storage Room",
    "description": """DESCRIPTION""",
    "exits": {"south": "RoomLandingLeft"}
}

room_child_bedroom = {
    "name": "Child's Bedroom",
    "description": """DESCRIPTION""",
    "exits": {"north": "RoomLandingLeft"}
}

room_bathroom = {
    "name": "Bathroom",
    "description": """DESCRIPTION""",
    "exits": {"south": "RoomLandingRight", "west": "RoomMasterBedroom"}
}

room_hidden = {
    "name": "Hidden Room",
    "description": """DESCRIPTION""",
    "exits": {"north", "RoomLandingRight"}
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
    "RoomStorage": room_storage,
    "RoomChildBedroom": room_child_bedroom,
    "RoomBathroom": room_bathroom,
    "RoomHidden": room_hidden,
}
