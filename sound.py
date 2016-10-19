import time

try:
	import pygame

	SOUND_PATH = "./sounds/"
	sound_files = ["door_open.wav", "door_slam.wav", "music_box.wav", "music_box_distant.wav"]
	loaded_sounds = {}

	def load_sounds():
		print("Loading sound files...")
		#pygame.mixer.init(44100, -16, 2, 4096)
		#time.sleep(10)
		pygame.init()
		for name in sound_files:
			loaded_sounds[name] = pygame.mixer.Sound(SOUND_PATH + name)
		print("Done loading sounds")

	def play_sound(name, loop=0):
		loaded_sounds[name].play(loop)
		
	def play_music(stype):
		if stype == "distant":
			loaded_sounds["music_box_distant.wav"].set_volume(1.0)
			loaded_sounds["music_box.wav"].set_volume(0.0)
		else:
			loaded_sounds["music_box_distant.wav"].set_volume(0.0)
			loaded_sounds["music_box.wav"].set_volume(1.0)
		 
except:
	def load_sounds():
		print("Sound disabled. Please install pygame.")
	def play_sound(name):
		pass
	def play_music(name):
		pass
