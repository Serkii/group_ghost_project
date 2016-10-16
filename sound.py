import pygame

SOUND_PATH = "./sounds/"
sound_files = ["door_open.wav"]
loaded_sounds = {}

def load_sounds():
	print("Loading sound files...")
	pygame.init()
	for name in sound_files:
		loaded_sounds[name] = pygame.mixer.Sound(SOUND_PATH + name)
	print("Done loading sounds")

def play_sound(name):
	loaded_sounds[name].play()
