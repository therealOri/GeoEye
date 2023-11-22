import os
import requests
import re
import beaupy
from beaupy.spinners import *
import shutil


def clear():
	os.system("clear||cls")


def main():
	url = beaupy.prompt("Url: ")
	clear()
	spinner = Spinner(DOTS, "Searching for latitude & longitude...")
	spinner.start()

	response = requests.get(url)
	res = response.text[200:420].replace("null","")
	pattern = r"-*\d+\.\d+,-*\d+\.\d+"
	matches = re.findall(pattern,res)[0].split(',')
	spinner.stop()

	return matches




if __name__ == '__main__':
	clear()
	cords = main()
	choice = beaupy.confirm("Do you want to open google maps with the cords?")

	if not choice:
		clear()
		print(cords)
	else:
		clear()
		print(cords)
		browsers = ["firefox", "chrome", "brave", "safari", "msedge"]
		default_browser = "xdg-open"
		for browser in browsers:
			if shutil.which(browser):
				os.system(f"{browser} 'https://www.google.com/maps/place/{cords[0], cords[1]}'")
				break
		else:
			os.system(f"{default_browser} 'https://www.google.com/maps/place/{cords[0], cords[1]}'")


