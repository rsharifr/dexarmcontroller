from pydexarm import Dexarm
from os import listdir
from os import path
import random
import time

robotConnected = True

# Connect to robot
if robotConnected:
    '''windows'''
    # dexarm = Dexarm(port="COM67")
    '''mac & linux'''
    dexarm = Dexarm(port="/dev/ttyACM0")

# List all files in the patterns directory
patternFolder = "patterns"
listOfPatterns = listdir(patternFolder)
print("These files were found in the folder "+patternFolder+":")
print(listOfPatterns)


def drawPattern(pattern):
    print("Executing the pattern:") # prints the name of the pattern file
    print(pattern)
    print(path.join(patternFolder,pattern))
    with open(path.join(patternFolder,pattern), 'r') as file:
        # Read each line in the file
        for line in file:
            line = line.strip(); # .strip() removes any leading/trailing whitespace.
            if line=="" or line[0]==";":
                continue
            command = line.strip()+"\r\n"  # we need end of line characters \n and \r. Let's have both just to be sure
            print(command)  
            if robotConnected:
                # send it to robot                
                dexarm._send_cmd(command)  

def resetPage(): # a script to rest the page.
    drawPattern('../reset.gcode')

# Loop forever
while True:
    resetPage()
    thisPattern = random.sample(listOfPatterns, 1) # pick 1 random pattern from the list
    drawPattern(thisPattern[0])
    time.sleep(60)


