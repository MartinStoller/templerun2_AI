import csv
import time
import itertools
import collections
queue = collections.deque([[1, 2], [3, 4]])
last_line = 0
last_was_zero = False
i = 0
with open("maindatabase.csv", "r") as main:
    reader1 = csv.reader(main)
    with open("doubled_maindatabase.csv", "w", newline="") as doubled:
        writer = csv.writer(doubled, dialect="excel")
        for line in reader1:
            if last_line != 0 and last_was_zero == True and int(line[-1]) != 0:
                #print(last_line)
                last_line[-1] = int(line[-1])
                #print(last_line)
            if last_line != 0:
                writer.writerow(last_line)
            if int(line[-1]) == 0:
                last_was_zero = True
            else:
                last_was_zero = False

            last_line = line