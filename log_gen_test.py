import pandas as pd
import csv
import requests
import datetime
'''
data = pd.DataFrame({"A" : ["John","Deep","Julia","Kate","Sandy"], 
                     "MonthSales" : [25,30,35,40,45]})
garbo = {"A" : ["blarg","hoppy", "spork"], "B" : ["cat","dog","spam"]}


garbo["A"].append("BOING")
garbo["B"].append("BLIGGITY")
garbo["test"] = []

garbo["test"].append("1")
garbo["test"].append("2")
garbo["test"].append("3")
garbo["test"].append("4")


data2 = pd.DataFrame(garbo)

print(data2)
'''

site = requests.get("https://www.google.com")

stuff = ((site.text).split('<'))



bob = open("test2.csv",'r') 

bob_string = bob.read()

garbo = {}

for i in bob_string.split(','):
	#print(i)
	garbo[i] = []
print(garbo)

for i,v in garbo.items():
	garbo[i].append(str(datetime.datetime.now()))
	for thing in stuff:
		garbo[i].append(thing)
	#garbo[i].append("3")
	#garbo[i].append("4")
	#print(i,v)

data = pd.DataFrame(garbo)

print(data)
