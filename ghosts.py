from combatscenarios import *

test_ghost = {

	"id": "testghost",

	"name": "Spookman, the Test Ghost",

	"desc": """It's a person with a white sheet over their head. The letters 'WIP' are
	painted on the front of the sheet, underneath the eye-holes. Spooky.""",

	"intro": "I AM THE TEST GHOST. YOU DON'T STAND A GHOST OF A CHANCE AGAINST ME.",

	"intro2": "AH, YOU HAVE RETURNED! WHAT'S WRONG? YOU LOOK LIKE YOU'VE SEEN A GHOST!",

	"player_escaped": False,

	"combat_skill": 7,

	"hp": 100,

	"peace_conditions_met": 0,

	"damage_text": "Your shot hits the test ghost! It hurts him a bit.",

	"onhit_text": "The ghost punches you in the face, and giggles to itself.",

	"death_text": "The ghost exclaims a surprisingly deadpan 'ouch', then falls over dead. Was it really a ghost?"
	
}

ghost_dog = {

	"id": "ghostdog",

	"name": "Etheral Doberman",

	"desc": """In front of you is a very aggressive looking Doberman. It is hard to get its exact figure as it phases in
	and out of reality. The dog bears its teeth at you and looks ready to pounce.""",

	"intro": "Although usually you shrug off ghosts as supernatural, the beast in front of you seriously shakes your grounding in reality.",

	"intro2": "The Dog still stands in front of the fireplace it shifts its footing the moment it sees you and resumes growling at you.",

	"player_escaped": False,

	"combat_skill": 7,

	"hp": 50,

	"peace_conditions_met": 0,

	"damage_text": "The Dog lets out a slight whelp and retreats back slightly, he hasn’t given up yet however.",

	"onhit_text": "The Dog pounces at you, jaw open, it bites down on your leg and you barely manage to kick him back.",

	"death_text": "The Doberman lets out a constant whelp and dives towards the window, you expect the glass to smash but instead the Doberman phases through it and disappears into the garden. You doubt you’ll see him again."
	
	#Located in the Living Room
	#Need a peaceful way of dealing with him, probably feed him an item (maybe one of the pizza's?)
}

ghost_Pinkerton = {

	"id": "pinkerton",

	"name": "Sir Pinkerton",

	"desc": """The Man has put down his knife and fork and stands up from his chair. He wears a typical dinner jacket and accompanying smart trousers.
	Through his jacket it as if you can see an outline of all of the organs in his body, his stomach is particularly black. His hands are placed behind
	his back but his eyes dart between you and the assortment of knives and forks on the table.""",

	"intro": "Ah another guest, welcome, I am Sir Pinkerton the rightful head of this household.  I do hope you can be more civil than the group before you. I would hate to have to forcibly remove you from the premises.",

	"intro2": "Ah? You have returned. I suppose we have some unfinished business to attend to",

	"player_escaped": False,

	"combat_skill": 7,

	"hp": 100,

	"peace_conditions_met": 0,

	"damage_text": "Sir Pinkerton staggers back as you take the picture, however he quickly regains his posture and poises ready to attack.",

	"onhit_text": "Sir Pinkerton picks up a knife and throws it at you.",

	"death_text": "Sir Pinkerton shivers and looks to you with confusion, he slowly fades into the ether clutching at his stomach."
	
	#Located in the Dining Room
	#Peacefully dealt with by conversing with him and explaining to him that he his dead and deducing he has been posioned.
}

ghost_Chef = {

	"id": "chef",

	"name": "The Burnt Chef",

	"desc": """The ghost in front of you is mostly opaque save for his face which suffers from great burns. From his silhouette you can make out his chef
	uniform complete with an unnecessarily tall hat that must fall off anytime he walks through a door. In his right hand he holds a very real meat clever
	and fiddles with rat poison in his other hand.""",

	"intro": " ‘Might you be the extra hand I asked my brother for? It might seem kind of him to offer me a job but let me tell you I should have been the one to inherit this place!’ He glances at the poison in his hand and the meat behind him ‘You have seen too much.’",

	"intro2": "Don’t think I will let you leave so easily this time!",

	"player_escaped": False,

	"combat_skill": 9,

	"hp": 150,

	"peace_conditions_met": 0,

	"damage_text": "The Chef staggers and grips his face in pain.",

	"onhit_text": "The Chef charges at you with his cleaver and slashes at you.",

	"death_text": "The Chef erupts into flame. Screaming, he dashes towards the sink, but disappears into thin air before he can reach it."
	
	#Located in the Kitchen
	#Unkown how to peacefully deal with, perhaps with an item given by Pinkerton?
}