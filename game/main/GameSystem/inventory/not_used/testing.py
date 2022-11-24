import csv 
with open("export.csv", newline="") as f: 
  csvreader = csv.reader(f) 
  for row in csvreader: 
    i = int(column[0]) # first column of the row 
    print (i) 
