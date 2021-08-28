import csv
import time

with open("database1.csv", "r") as database1:
    with open("maindatabase.csv", "a+", newline="") as maindatabase:
        writer = csv.writer(maindatabase, dialect="excel")
        reader = csv.reader(database1)
        # length = (len(list(reader)))
        # print(length)
        # time.sleep(999)
        i = 0
        print("Warning! You are about to modify the training main database! You have 6 seconds to stop the program!")
        print("make sure that the amount of rows is up to date and the database1 file was cleared before the last game")

        time.sleep(6)
        for row in reader:
            if len(row) >= 4:
                writer.writerow(row)
                i +=1
            if i > 1300:
                break

