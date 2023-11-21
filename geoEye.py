import os
import requests
import re


url = input('URL Here: ')
# os.system('clear||cls')
response = requests.get(url)


# This isn't very helpful as the data gathered can be longer or shorter which results in valuable data being cut off at idk where. Anyone is more than welcome to push a request and change this code to hopefully make it better and more useful.
# I need a better way to either filter out everything I don't need, or to find a way to specifically grab what I need from the url/response then print it.
# As of rn, the values below should be enough to give you a lattitude, a longitude, town name/location and maybe a road name and or a road number. You can change this if you need.
res = response.text[200:420].replace("null","")

pattern = r"-*\d+\.\d+,-*\d+\.\d+"
matches = re.findall(pattern,res)[0].split(',')

print(matches)
os.system(f"firefox 'https://www.google.com/maps/place/{matches[0],matches[1]}'")
