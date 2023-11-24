import os
import requests
import re
import beaupy
import webbrowser
from beaupy.spinners import *


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
	coords = main()
	choice = beaupy.confirm(f"Do you want to open Google Maps with the Coordinates {coords[0]}, {coords[1]} in your browser?")

	if not choice:
		clear()
		print(f"{coords[0]}, {coords[1]}")
	else:
		clear()
		print(f"{coords[0]}, {coords[1]}")
		webbrowser.open(f"https://www.google.com/maps/place/{coords[0], coords[1]}")

