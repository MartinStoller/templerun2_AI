import csv
import time

with open("cleaned_doubled_maindatabase.csv", "r") as database1:
    reader = csv.reader(database1)
    i = 0
    n = 0
    for row in reader:
        n += 1
        if int(row[-1]) == 0:
            i += 1
    
    print("No action percentage:")
    print(i/n)
    print(n)
