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
    "description": """DESCRIPTION""",
    "exits": {"downstairs": "RoomLobby", "north": "RoomMasterBedroom", "east": "RoomLandingRight", "west": "RoomLandingLeft"},
    "items": []
}

room_landing_left = {
    "name": "The Left of the Landing",
    "description": """DESCRIPTION""",
    "exits": {"east": "RoomLandingCentre", "north": "RoomStorage", "south": "RoomChildBedroom"},
    "items": []
}

room_landing_right = {
    "name": "The Right of the Landing",
    "description": """DESCRIPTION""",
    "exits": {"west": "RoomLandingCentre", "north": "RoomBathroom", "south": "RoomHidden"},
    "items": []
}

room_master_bedroom = {
    "name": "Master Bedroom",
    "description": """DESCRIPTION""",
    "exits": {"south": "RoomLandingCentre", "east": "RoomBathroom"},
    "items": []
}

room_storage = {
    "name": "Storage Room",
    "description": """DESCRIPTION""",
    "exits": {"south": "RoomLandingLeft"},
    "items": []
}

room_child_bedroom = {
    "name": "Child's Bedroom",
    "description": """DESCRIPTION""",
    "exits": {"north": "RoomLandingLeft"},
    "items": []
}

room_bathroom = {
    "name": "Bathroom",
    "description": """DESCRIPTION""",
    "exits": {"south": "RoomLandingRight", "west": "RoomMasterBedroom"},
    "items": []
}

room_hidden = {
    "name": "Hidden Room",
    "description": """DESCRIPTION""",
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
    "RoomStorage": room_storage,
    "RoomChildBedroom": room_child_bedroom,
    "RoomBathroom": room_bathroom,
    "RoomHidden": room_hidden
}
