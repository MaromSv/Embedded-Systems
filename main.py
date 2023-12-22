#Author(s): Marom Sverdlov 
#Date last modified: 01/06/2022

import gui
# from gpiozero import Servo
# from time import sleep

### Variable declaration:
blackNeeded = False
whiteNeeded = False
whiteDisks = 0
blackDisks = 0
diskColor = "none"#False -> white, True -> black
kickTimer = 100; #In ms, NOTE: We should play around with this and see what works
errorCode = 0; #Number from 0 - x where x is the amount of errors we can identify

###Main sequence:


def main():
    GetInput() #Get Input from GUI i.e wait for start to be clicked
    IsBlackOrWhiteNeeded() #Update values of blackNeeded and whiteNeeded

    while (blackNeeded or whiteNeeded): #Only when both blackNeeded and whiteNeeded are False program ends

        if(DetectError()): #If error detected initialize sequence
            ErrorSequence()
        
        if (DiskDetected()):
            IdentifyDiskColor() #update value of diskColor
            if (((diskColor == "white") and whiteNeeded) or ((diskColor == "black") and blackNeeded)): #Just like in the automata, if a disk color is needed and present its punched
                sleep(kickTimer) #Period between sensing and kicking the disk TODO:Finetune it
                kickDisk() #Kick the disk into the basket 
                updateCount(diskColor) #Updates the count of the remaining disks needed and sends it to the GUI
                IsBlackOrWhiteNeeded() #Recomputes blackNeeded and whiteNeeded
        
    PrintOnScreen("Finished order \n -Press the Reset button to start a new order- \n")

###Function definition:

def IsBlackOrWhiteNeeded():
    global blackNeeded 
    blackNeeded = IsBlackNeeded()
    global whiteNeeded
    whiteNeeded = IsWhiteNeeded()


def IsBlackNeeded(): #Checks if Black disks stil needed
    if (int(blackDisks) > 0):
        return True
    else:
        return False


def IsWhiteNeeded():#Checks if White disks stil needed
    if (int(whiteDisks) > 0):
        return True
    else:
        return False

def kickDisk():
    print("kick")
    # servo = Servo(17)
    # sleep(0.5)
    # servo.max()
    # servo.min()
    # sleep(0.5)


def updateCount(color):
    if (color == "black"): #If disk was black
        blackDisks = blackDisks - 1
    elif (color == "white"): #If disk was white
        whiteDisks = whiteDisks - 1


def GetInput():
    exec(open('gui.py').read())
  

def PrintOnScreen(str):
    print(str)


def DiskDetected():
    #---Code to detect disk---
    return False

def IdentifyDiskColor():
    print("IdentifyingDiskColor")
    #---Code to identify disk color---

def DetectError():
    return False

def IdentifyError(errorCode):
    str = ""

    if (errorCode == 0):
        str = "Error 0"
    elif (errorCode == 1):
        str = "Error 1"
    elif (errorCode == 2):
        str = "Error 2"

    return str


def ErrorSequence():
    PrintOnScreen(IdentifyError(errorCode))
    #To be completed!

### Calling main
main()