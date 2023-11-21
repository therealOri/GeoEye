import os
import requests
import re


url = input('URL Here: ')
response = requests.get(url)

res = response.text[200:420].replace("null","")

pattern = r"-*\d+\.\d+,-*\d+\.\d+"
matches = re.findall(pattern,res)[0].split(',')

print(matches)
# os.system(f"firefox 'https://www.google.com/maps/place/{matches[0],matches[1]}'")
