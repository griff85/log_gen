import pandas as pd
import csv
import requests
#import datetime


site = requests.get("https://www.google.com")

stuff = ((site.text).split('<'))



bob = open("test2.csv",'r') 

bob_string = bob.read()

garbo = {}

for i in bob_string.split(','):
	garbo[i] = []
print(garbo)

for i,v in garbo.items():
	#garbo[i].append(str(datetime.datetime.now()))
	for thing in stuff:
		garbo[i].append(thing)


data = pd.DataFrame(garbo)

print(data)

data.to_csv("test3.csv", header = True, index = False)
