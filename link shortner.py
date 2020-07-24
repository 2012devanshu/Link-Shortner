
__author__ : "@rockdevu"

# This program is used to shorten the URLs.

import pyshorteners as short

url = input("Please enter the URL : ")

s = short.Shortener()

print("Your link is ready : ",s.tinyurl.short(url))
