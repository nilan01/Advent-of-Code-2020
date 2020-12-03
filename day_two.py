# Advent of Code Day 2
# December 2, 2020

def d2():
    #print("hi")
    globalcounting = 0
    with open("day_two.txt", "r") as f:
        for line in f:
            linesplit = line.split(" ")
            rangesplit = linesplit[0].split("-")
            rangemin = int(rangesplit[0]) #range minimum
            rangemax = int(rangesplit[1]) #range maximum
            lettersplit = linesplit[1].split(":")
            letter = lettersplit[0] #stored letter

            counting = 0
            for password in linesplit[2]:
                if letter is password:
                    counting += 1
            if counting >= rangemin and counting <= rangemax:
                globalcounting += 1

        print(globalcounting)

def d2b():
    globalcounting = 0
    with open("day_two.txt", "r") as f:
        for line in f:
            linesplit = line.split(" ")
            rangesplit = linesplit[0].split("-")
            firstpos = int(rangesplit[0])
            secondpos = int(rangesplit[1])
            lettersplit = linesplit[1].split(":")
            letter = lettersplit[0]

            password = linesplit[2]
            if letter is password[firstpos - 1] or letter is password[secondpos - 1]:
                if password[firstpos - 1] is not password[secondpos - 1]:
                    globalcounting += 1

        print(globalcounting)