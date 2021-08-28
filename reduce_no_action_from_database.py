import csv
import random

with open("doubled_maindatabase.csv", "r") as maindatabase:
    with open("cleaned_doubled_maindatabase.csv", "w", newline="") as cleaned:
        writer = csv.writer(cleaned, dialect="excel")
        reader = csv.reader(maindatabase)
        for row in reader:
            if int(row[-1]) == 0:
                n = random.randint(0, 9)
                if n > 7:
                    writer.writerow(row)
            elif int(row[-1]) in [1, 2, 3, 4, 5, 6]:
                writer.writerow(row)

