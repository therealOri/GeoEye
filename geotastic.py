import requests as re
import os

url = input('URL Here: ')
os.system('clear||cls')
response = re.get(url)


# This isn't very helpful as the data gathered can be longer or shorter which results in valuable data being cut off at idk where. Anyone is more than welcome to push a request and change this code.
# I need a better way to either filter out everything I don't need, or to find a way to specifically grab what I need from the url/response then print it.
# As of rn, the values below should be enough to give you a lattitude, a longitude, country name/location and maybe a road number. You can change this if you need.
res = response.text[200:420]
print(res.replace("null", ""))
