try:
	import pygame

	SOUND_PATH = "./sounds/"
	sound_files = ["door_open.wav", "door_slam.wav", "music_box.wav", "music_box_distant.wav"]
	loaded_sounds = {}

	def load_sounds():
		print("Loading sound files...")
		pygame.init()
		pygame.mixer.init(44100, -16, 1, 1024)
		for name in sound_files:
			loaded_sounds[name] = pygame.mixer.Sound(SOUND_PATH + name)
		print("Done loading sounds")

	def play_sound(name):
		loaded_sounds[name].play()
		
	def play_music(name):
		pygame.mixer.music.load(SOUND_PATH + name)
		pygame.mixer.music.play(10000) # infinity
except:
	def load_sounds():
		print("Sound disabled. Please install pygame.")
	def play_sound(name):
		pass
	def play_music(name):
		pass
