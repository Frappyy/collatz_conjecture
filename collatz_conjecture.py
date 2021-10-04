from os.path import exists
import os
import atexit

origNum = 1
number = 1
savedIter = 0
iterations = 0
ccs = os.path.dirname(os.path.abspath(__file__)) + "\\collatz_conjecture_save.txt"

if exists(ccs):
    file = open(ccs, "r")
    origNum = int(file.readline())
    content = file.readlines()[0]
    savedIter = int(content)
    print(origNum,"|",savedIter,ccs)
    file.close()

def exiting():
    file = open(ccs, "w")
    file.write(str(origNum))
    file.write(str("\n"))
    file.write(str(savedIter))
    file.close()
    print(origNum,"|",savedIter)
    print("Exiting!")

atexit.register(exiting)

while True:
    if number == 1:
        origNum += 1
        number = origNum
        if iterations > savedIter:
            savedIter = iterations
            print(origNum,"|",savedIter)
        iterations = 0

    elif number % 2 == 0:
        number = number / 2
        iterations += 1

    else:
        number = number * 3 + 1
        iterations += 2

