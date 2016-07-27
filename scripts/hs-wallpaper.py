# Author: Areeb Beigh
# Created: 10th April 2016

'''
Chooses a random image file from the directory specified in the config.ini 
[hs-wallpaper] section and sets it as the desktop background 
'''

import ctypes
import os
import random

from initialize import *

# Gets the directory containing the wallpapers from the config.ini 
# [hs-wallpaper] seciton
wallpaperDirectory = Config.get("hs-wallpaper", "directory")

def main():
	execute()

def getWallpapers(givenDir):
	"""Iterates over the directory of wallpapers tree and returns a list of 
	the wallpapers / images"""
	files = os.listdir(givenDir)
	wallpapers = []

	for file in files:
		file = os.path.join(givenDir, file)
		extensions = [".jpg", ".png"]

		# Calls check() recursively on subdirectories
		if(os.path.isdir(file)):
			wallpapers.extend(getWallpapers(file))
		
		# If the file is an image file then ...
		elif(os.path.splitext(file)[1].lower() in extensions):
			wallpapers.append(file)

	return wallpapers

def execute():
	# If the wallpaper directory is specified in config.ini then ...
	if (wallpaperDirectory):
		wallpapers = getWallpapers(wallpaperDirectory)

		# Chooses a random wallpaper from the list of wallpapers
		randomWallpaper = random.choice(wallpapers)

		print("{0} Setting {1} as random desktop wallpaper...".format(
			whiteSpace, 
			randomWallpaper))

		SPI_SETDESKWALLPAPER = 20

		ctypes.windll.user32.SystemParametersInfoW(
			SPI_SETDESKWALLPAPER, 
			0, 
			randomWallpaper, 
			0)

	# If the wallpaper directory is not specified in config.ini then ...
	else:
		print("{0} No directory specified in the config file".format(whiteSpace))

if __name__ == "__main__":
	main()