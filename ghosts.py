from items import *

killed_ghost_count = 0


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

	"peace_text" : "The dog wags its tail and pants. You see the dog slowly disappear into the ether",

	"damage_text": "The Dog lets out a slight as you blast him with your proton gun, he has not given up yet however.",

	"onhit_text": "The Dog pounces at you, jaw open, it bites down on your leg and you barely manage to kick him back.",

	"death_text": "The Doberman lets out a constant whelp and dives towards the window, you expect the glass to smash but instead the Doberman phases through it and disappears into the garden. You doubt you will see him again.",
	
	"items_wanted": [item_garlic],

	"loot": [item_dogcollar],
	#Located in the Living Room
	#Need a peaceful way of dealing with him, probably feed him an item (maybe one of the pizza's?)
	"conversation": {
		"speech": "Hello, I'm a ghost!",
		"responses": {
			"hello": {
				"speech": "Nice to meet you! What's your favourite colour?",
				"responses": {
					"red": {
						"speech": "That's a nice colour!",
						"function": "ghost_peace"
					},
					
					"blue": {
						"speech": "You have poor taste."
					}
				}
			},
			"eeeww": {
				"speech": """How dare you insult me, puny human!

*The ghost slays you with a single touch*""",
				"function": "hurt_player",
				"responses": {
					"test": {
						"speech": "hello world"
					},
					"test2": {
						"speech": "bye world"
					}
				}
			}
		}
	}
}

ghost_Pinkerton = {

	"id": "pinkerton",

	"name": "Sir Pinkerton",

	"desc": """The Man has put down his knife and fork and stands up from his chair. He wears a typical dinner jacket and accompanying smart trousers.
	Through his jacket it as if you can see an outline of all of the organs in his body, his stomach is particularly black. His hands are placed behind
	his back but his eyes dart between you and the assortment of knives and forks on the table.""",

	"intro": "'Ah another guest, welcome, I am Sir Pinkerton the rightful head of this household.  I do hope you can be more civil than the group before you. I would hate to have to forcibly remove you from the premises.'",

	"intro2": "'Ah? You have returned. I suppose we have some unfinished business to attend to'",

	"player_escaped": False,

	"combat_skill": 7,

	"hp": 100,

	"peace_conditions_met": 0,

	"peace_text" : "'Thank you for enlightening me' Sir Pinkerton bows and disappears into thin air",

	"damage_text": "Sir Pinkerton staggers back as you fire at him, however he quickly regains his posture and poises ready to attack.",

	"onhit_text": "Sir Pinkerton picks up a knife and throws it at you.",

	"death_text": "Sir Pinkerton shivers and looks to you with confusion, he slowly fades into the ether, clutching at his stomach.",

	"loot": [item_laudanum],

	"conversation": {
		"speech": "What reason do you Have for interrupting my meal? I'd rather not have to resort to this violence.",
		"responses": {
			"You realise there's nothing on your plate right?": {
				"speech": "What are you talking about? This meal was made by my brother, I hired him as a chef here. He lacks many talents but at least he can cook, there's certainly an odd taste to it however.",
				"responses": {
					"Who is your brother?": {
						"speech": "My Brother? He cooks well enough but he has always resented me since I inherrited the house, he may be older but he did little for the family.",
						"responses": {
							"Could he have poisoned it?": {
								"speech": "You can't possibly believe he poisoned it!",
								"responses": {
									"It's hard to believe but you are a Ghost, take a look infront of you there's nothing on your plate":{
										"speech": "I'm dead? That explains a lot, if I am truly to pass peacefully, find my brother and avenge me",
										"function": "ghost_peace",
									},
									"Oh no of course not, maybe he's just such a terrible cook.":{
										"speech":"Such insolence!",
										"function": "hurt_player",
									}
								},
							},
						},
					},
					
					"What do you mean it tastes funny?": {
						"speech": "It does taste sort of off today when he cooks so well. Almost acidic...",
						"responses": {
							"Could he have poisoned it?": {
								"speech": "You can't possibly believe he poisoned it!",
								"responses": {
									"It's hard to believe but you are a Ghost, take a look infront of you there's nothing on your plate":{
										"speech": "I'm dead? That explains a lot, if I am truly to pass peacefully, find my brother and avenge me",
										"function": "ghost_peace",
									},
									"My mistake maybe he's just a bad cook.":{
										"speech":"Such insolence!",
										"function": "hurt_player",
										},
								},
							},
						},
					},
				},
			},
			"Is the dog in the living room yours?": {
				"speech": """Ah have you met the mutt? My Brother insisted he come with him the flea ridden thing.
I bearly tolerate him, we shall speak no more of him""",
			},
			"LEAVE conversation": {
				"speech": "Have we nothing more to speak off? Be gone then.",
			}
		}
	}
	#Located in the Dining Room
	#Peacefully dealt with by conversing with him and explaining to him that he his dead and deducing he has been posioned.
}

ghost_Chef = {

	"id": "chef",

	"name": "The Burnt Chef",

	"desc": """The ghost in front of you is mostly opaque save for his face which suffers from great burns. From his silhouette you can make out his chef
	uniform complete with an unnecessarily tall hat that must fall off anytime he walks through a door. In his right hand he holds a very real meat clever
	and fiddles with rat poison in his other hand.""",

	"intro": " 'Might you be the extra hand I asked my brother for? It might seem kind of him to offer me a job but let me tell you I should have been the one to inherit this place!' He glances at the poison in his hand and the meat behind him 'This isn't what it looks like!'",

	"intro2": "'Don't think I will let you leave so easily this time!'",

	"player_escaped": False,

	"combat_skill": 9,

	"hp": 150,

	"peace_conditions_met": 0,

	"peace_text" : "The Chef quickly turns around and returns to chopping attempting to hide the tears flowing down his face. He slowly fades away and once he's gone his cleaver falls to the ground.",

	"damage_text": "The Chef staggers as you fire on him and grips his face in pain.",

	"onhit_text": "The Chef charges at you with his cleaver and slashes at you.",

	"death_text": "The Chef erupts into flame. Screaming, he dashes towards the sink, but disappears into thin air before he can reach it.",

	"items_wanted": [item_dogcollar],

	"loot": [item_poison,item_cleaver],
	
	"conversation": {
		"speech": "I use this poison for the rats in the house! That's it!",
		"responses": {
			"The food behind you wouldn't be poisoned would it?": {
				"speech": "No of course not! Well... it is but it wasn't me! I only noticed it now!",
				"responses": {
					"That sounds like a lie to me!": {
						"speech": "You might no believe me but I can make sure you tell no one else",
						"function": "hurt_player",
					},
					"Then who poisoned it?": {
						"speech": "I...I don't know, but you have to find out! Someone is trying to kill the people of this house",
						"responses" : {
							"Well... the thing is you're already dead... you're a ghost": {
								"speech":"I'm a what?",
								"responses" : {
									"You're a ghost Chef..." : {
										"speech":"I... I am... Look what ever is going on here you have to find out what happened here, take whatever will help you from the kitchen",
										"function": "ghost_peace",

									}

								}
							},
						},
					},
				},
			},
			"LEAVE conversation": {
				"speech": "You won't tell anybody I posioned anyone!",
			},
			"The dog in the living room is yours isn't it?" : {
				"speech": "You saw his grave from the window I take it? Loyal as anything but stupid too, I do miss him",
				"responses" : {
					"No, no no... He wasn't in a grave, I did have to put him down however":{
						"speech" : "how dare you!",
						"function": "hurt_player",
					},
					"Yeah... well... shame about that" : {
						"speech" : ""
					} 
				},
			},
		},
	},
	
	#Located in the Kitchen
	#Unkown how to peacefully deal with, perhaps with an item given by Pinkerton?
}

ghost_Lady = {

	"id": "lady",

	"name": "The Lady of the House",

	"desc": """A fair woman, brushes her silver hair at the dressing table, and occasionally glances in your direction.
	She adorns a beautiful dress that would only be fitting at a 19th century re-enactment fair. There is a blue ring around her neck.""",

	"intro": "'Do you not realise how rude it is to enter a lady's room uninvited, you servants are so uncouth, you should leave now'",

	"intro2": "'You again? Were it not for my husband I'd have you fired immediately, instead I suppose I should instill some discipline.'",

	"player_escaped": False,

	"combat_skill": 14,

	"hp": 150,

	"peace_conditions_met": 0,

	"peace_text" : "The Lady sits back at her desk and continues to brush her hair, slowly fading away after every brush",

	"damage_text": "The Lady's dress tears as you fire at her, revealing her flayed and burnt flesh underneath.",

	"onhit_text": "The Lady rises from her seat and scratches you with her nails.",

	"death_text": "You see the skin melts from her face as she claws at herself, you turn your head away but when you look back she is gone.",

	"loot": [item_brooch,item_ghostbook],
	
	"conversation" : {
		"speech" :"What reason do you have for entering my room uninvited?",
		"responses": {
			"Forgive me, my lady, but I'm here to deliver this pizza" :{
			"speech": "Pizza? what on earth has my husband bought now. Regardless you should be downstairs not here",
			},
			"Oh sorry I thought that this was the Bathroom, I'll leave now.":{
				"speech":"Please do.",
			},
			"I'm here investigating a haunting" :{
				"speech" : "A haunting? what superstition, there is no such thing as ghosts",
				"responses" : {
				"But M'lady you ARE a ghost":{
					"speech":"What rubbish are you spewing, be gone with you",
					"function": "hurt_player",
					},
				"I used to believe that too, but the things in this house have me questioning that, you for example." :{
					"speech" : "What do you mean by me?",
					"responses" : {
						"Well you're not actually alive, neither your husband downstairs, someone killed you and I'm trying to figure out who":{
							"speech" : "Not alive? You must jest, and who would want to kill us?",
							"responses" : {
								"That's what I'm trying to figure out, someone put rat poison in your food." :{
								"speech" : "My! I suppose if my husband let you in it must be serious, I'll stay out of your way but none of that ghost business, you'll scare our daughter.",
								"function": "ghost_peace",
								},
								"What about the Chef? He is the next in line to own the Mansion." : {
								"speech" : "That's my Brother-in-Law you are speaking of! How dare you!",
								"function": "hurt_player",
								},
							},
						},
						"What I mean is that your beauty stunned me M'lady": {
							"speech":"Such weak flattery will not work on me, I am married after all.",
							"function" : "hurt_player",
							},
						},
					},
				},
			},
		},
	},
}

ghost_Poltergeist = {

	"id": "poltergeist",

	"name": "Library Poltergeist",

	"desc": """What seems to be a neglected library suddenly comes to life when you enter, the books rise from the ground and circle the air around the armchair. The books spin violently.""",

	"intro": "At your presence some of the books stop spinning and launch themselves at you.",

	"intro2": "You return to the books still circling the armchair",

	"player_escaped": False,

	"combat_skill": 1,

	"hp": 1000,

	"peace_conditions_met": 0,

	"peace_text" : "The books slowly return to their rightful place on the shelves.",

	"damage_text": "You fire your proton gun at one of the books, disintegrating it. There are still an uncountable amount of books left.",

	"onhit_text": "A Book is flung at you.",

	"death_text": "The remaining books in the room fall to the ground.",

	"items_wanted": [item_ghostbook],

	"loot": [item_childsbook],
	
	#Located in the Library
	#Difficult to deal with via combat, requires some sort of item

}


ghost_toys = {

	"id": "toys",

	"name": "Haunted Toy Soldiers",

	"desc": """There is an assortment of broken toy soldiers in the room, they have all been modified in grotesque ways. They guard a small bookshelf of children's books. One of the books is missing.""",

	"intro": "The toy soldiers stagger towards you, attempting to march to a beat matching the melody of the ballerina.",

	"intro2": "The toy soldiers are there in formation, ready for you.",

	"player_escaped": False,

	"combat_skill": 10,

	"hp": 250,

	"peace_conditions_met": 0,

	"peace_text" : "The Soldiers March in a collum towards the toy box, as the last one climbs in the box shuts.",

	"The books slowly return to their rightful place on the shelves"

	"damage_text": "A concentrated beam from your gun destroys a couple of the soldiers.",

	"onhit_text": "A Soldier clambers are your leg and stabs at your thigh with his sword",

	"death_text": "The remaining soldiers all fall down. The Ballerina still spins in the music box, although there is no longer an audience.",

	"items_wanted": [item_childsbook]
	
	#Located in the Childrens room
	#requires a book from the Library to defeat peacefully

}

ghost_julia = {

	"id": "julia",

	"name": "The Child",

	"desc": """A little girl circles the captured ghost busters on a tricycle in a scene you swear you've seen somewhere before she hums a tune similar to the one you heard from a music box. 
	She occasionally prods the Ghost busters with her wooden sword, and clutches a teddy bear head in her other arm.""",

	"intro": """'Oh another guest come to play with me! My name's Julia and I'm the head of the house now!
	 We should play a game, Daddy and Mommy won't be playing with me anymore and these people were getting boring so let's play!'""",

	"intro2": "'Oh good, Oh good you're back! I was hoping we could play some more!'",

	"player_escaped": False,

	"combat_skill": 15,

	"hp": 400,

	"peace_conditions_met": 0,

	"peace_text" : "'Congratulations! You really are a smart one, I've been stuck in this room for hundreds of years waiting for someone to complete the mystery.' Julia waves and slowly fades. 'Be sure to play with me again! Daddy, Mummy and Uncle get to go but I'm stuck here for eternity!' Julia disaperes from veiw, the ropes binding the Ghost Busters untangle themselves.",

	"damage_text": "You fire the proton cannon at Julia",

	"onhit_text": "'En garde!' Julias Wooden sword suddenly erupts in flames and she slashes at you",

	"death_text": "You hear a piercing scream as Julia is engulfed by a beam of light. The oppressing atmosphere throughout the mansion suddenly dissipates and the ropes on the ghost busters burn off too.",

	"conversation": {
		"speech" : "You're here to play right? How about a quiz, if you win I these guys go. If I win, you have to play with me forever",
			"responses" : {
				"Okay, I'll play your game.":{
					"speech" : "Goodie! First Question and lets start easy; what is the name of the house?",
					"responses" : {
						"Clearveiw Mansion" : {
							"speech" : "Ding Ding!, Correct! Next question: How did the dog die?",
							"responses" : {
								"The Dog died from rat poison." : {
								"speech" : "Ding Ding! Correct Again! Next Question: What happened to Mummy?",
								"responses" : {
									"She couldn't take the loss of Sir Pinkerton and hung herself." : {
										"speech" : "Ding Ding! You're on a roll! Final Question: What happened to Daddy?",
											"responses" : {
												"You poisoned your Father and blamed it on the Chef!" : {
													"speech" : "Ehehehe, you're correct! Daddy was a bully and wouldn't stop hitting me, I gave him a taste of his medicine and everyone blamed it on uncle!",
													"function": "ghost_peace",
												},
												"The Chef poisoned Sir Pinkerton to inherit the Mansion!": {
													"speech" : "Everyone believed that! It's not even true! Time for your punishment",
													"function": "hurt_player",
													},
												"Sick with life, Sir Pinkerton poisoned his own food, framing his Brother to take him down with him." :{
													"speech" : "Bzzzt! Wrong! Time for your punishment!",
													"function": "hurt_player",
												},
											},
									},
									"She was having an affair with the Chef and killed Sir Pinkerton to remarry.":{
										"speech" : "Bzzzt! Wrong! Time for your punishment!",
										"function": "hurt_player",
										},
									},
									"After Sir Pinkerton Died she locked herself in her bedroom untill she died." :{
										"speech" : "Bzzzt! Wrong! Time for your punishment!",
										"function": "hurt_player",
										},
								},
								"The Dog died of old age of course." :{
									"speech" : "Bzzzt! Wrong! Time for your punishment!",
									"function": "hurt_player",
								},
								"You killed it" : {
									"speech" : "Bzzzt! Wrong! Time for your punishment!",
									"function": "hurt_player",
								}
							},
						},
						"Pinkerton Mansion" : {
							"speech" : "Bzzzt! Wrong! Time for your punishment!",
							"function": "hurt_player",
						},
						"Tanglewood Mansion" : {
							"speech" : "Bzzzt! Wrong! Time for your punishment!",
							"function": "hurt_player",
						},

					},
				},
				"First I have some questions for you." : {
					"speech" : "Sure I'll awnser your questions!",
					"responses" : {
						"The Dog in the living room how did he die?" :{
							"speech" : "That should be obvious silly! Rat poison still hurts dogs, and they'll eat anything!",
						},
						"How did Sir Pinkerton Die?" : {
							"speech":"Daddy? He ate some bad food, Uncle cooks the food maybe it was him",
						},
						"The Lady in the Bedroom, what happened to her?" : {
							"speech" : "That would be mummy! She went away when daddy died."
						},
						"There was a chef in the Kitchen, what happened to him?" :{
						"Uncle? He was ran out of town by an angry mob when they found out he killed daddy!"
						}
					},
				},
				"I think I'll pass" :{
					"speech" : "Well you can't leave my house until you play with me!"
				}
			},
	}
	
	#Located in the Hidden room
	#unkown how to defeat, repair her teddy, find out she killed her parents.

}
