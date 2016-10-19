from items import *
from map import rooms

inventory = [item_pizza1,item_pizza2,item_garlic]

global current_room 
current_room = rooms["RoomOutside"]

sanity = 100

defense_multiplier = 1.0
attack_multiplier = 1.0

def calculate_stats():
	defense_multiplier = 1.0
	attack_multiplier = 1.0
	for item in inventory:
		if "attack" in item:
			attack_multiplier *= item["attack"]
		if "defense" in item:
			defense_multiplier *= item["defense"]
			
calculate_stats()
