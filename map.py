from items import *
#from npc import *

#Added some conditions that need to be implemented into the code

def lobby_on_enter(lobby):
    lobby.pop("on_enter", None)
    # *play sound*
    print("The front door slams shut behind you!")
    return True

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
    "exits": {"north": "RoomLobby"},
    "items": []
}

room_lobby = {
    "name": "Lobby",
    "description": """You are currently standing in the Lobby, the remains of the chandelier litter the
centre of the room, many tiles have fallen from the ceiling and the rotting floorboards
make it dangerous to navigate safely. Rays of light enter the room from the broken windows
at the front of the house. One ray illuminates a small bust situated underneath the balcony
of the second floor.""",
    #condition: "A strong ghostly aura blocks you from climbing the stairs"
    "exits": {"north": "RoomLandingCentre", "east": "RoomLiving", "west": "RoomDining"},
    "on_enter": lobby_on_enter,
    "items": [item_proton_gun]
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
    #condition: "In front of the fire a Doberman rests, when you try to focus your eyes on him he seemingly disappears."
    "exits": {"west": "RoomLobby"},
    "items": []
}

room_dining = {
    "name": "Dining Room",
    "description": """You stand now in the Dining Room, the wallpaper has peeled off in most places and only
a few candle holders are still attached to the walls. To your left you see the broken windows
that reveal the front of the house and your moped that helped you get here. The dining table
covers most of the room and can fit ten people. Smashed cutlery litters the table.""",
    #condition: """A ghostly figure sits at the head of the table, he seems to be eating something but there is nothing on his plate.
    #             Something tells you that you won't be getting into the kitchen until this man has been dealt with."""
    "exits": {"north": "RoomKitchen", "east": "RoomLobby"},
    "items": []
}

room_kitchen = {
    "name": "Kitchen",
    "description": """You are now in the Kitchen, encompassing the walls are various ruined cabinets each storing some
form of crockery most of which is ruined beyond repair. You know not how old this mansion is but you
are certain that the refrigerator is a new addition, it has a metallic sheen to it, uncharacteristic
of the rest of the house. There is a weird small of gas in the room and you feel it would be a bad idea
to turn on a light switch... that would be if the mansion had working electricity in the first place.""",
    #condition: "<Ghost here>"
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
