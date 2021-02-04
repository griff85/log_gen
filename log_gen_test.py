import pandas as pd
import csv
import requests
#import datetime


site = requests.get("https://www.google.com")

html = ((site.text).split('<'))



bob = open("headers.csv",'r') 

bob_string = bob.read()

dummy_data = {}

for i in bob_string.split(','):
	dummy_data[i] = []
print(dummy_data)

for i,v in dummy_data.items():
	#dummy_data[i].append(str(datetime.datetime.now()))
	for chunk in html:
		dummy_data[i].append(chunk)


data = pd.DataFrame(dummy_data)

print(data)

data.to_csv("test3.csv", header = True, index = False)
