import csv

list=[]
with open("main.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    list.append(row)