import os
import rumps
import time
from steem import Steem

rumps.debug_mode(True)

def secondsToText(seconds):
    hours, minutes = divmod(seconds, 3600)
    return str(hours + ":" + minutes)

def openAndWriteFile(tempuser):
    f = open("data.txt","w")
    f.write(tempuser)
    print("created file")
    f.close()

def readFile():
    if not os.path.isfile('./data.txt'):
        print("no file")
        openAndWriteFile()

    f = open("data.txt", "r")
    if f.mode == 'r':
        tempuser = str(f.read())
        print("Read user: " + tempuser)
    f.close()
    return tempuser

def getSteemPower(tempuser):
    return Steem().get_account(tempuser)['voting_power'] / 100


def calcSteempower(tempuser,boolInit):
    toFill = 100 - getSteemPower(tempuser)
    timeString = ""
        
    minToFill = round(toFill / (20/24/60),2)
    hourToFill = round(toFill / (20/24),2)
    dayToFill = round(toFill / 20,2)
    if hourToFill < 1:
        if minToFill < 45:
            stringFill = "<45m"
        elif minToFill < 30:
            stringFill = "<30m"
        elif minToFill < 15:
            stringFill = "<15m" 
        elif minToFill < 5:
            stringFill = "<5m"
        elif minToFill <= 0:
            stringFill = "~0m"
        else:
            stringFill = "<1h"
    else:
        hourToFill = round(toFill / (20/24))
        stringFill = "~" + str(hourToFill) + "h"

    return str(getSteemPower(tempuser)) + "% (" + stringFill + timeString + ")" 


firstCalc = True
startFill = 0
timeStart = 0
timeNow = 0
timeString = ""

class VotingPowerApp(rumps.App):
    globaluser = ''
    clicktext = 'Name'
    def __init__(self): 
        self.globaluser = globaluser = clicktext = readFile()
        if not self.globaluser:
            print("empty" + self.globaluser)
            clicktext = "SteemUser"
            titleValue = "Enter SteemName"
        else:
            titleValue = calcSteempower(self.globaluser,True)
            
        super(VotingPowerApp, self).__init__(titleValue)

    @rumps.clicked("Change " + clicktext)
    def openPreferences(self, _):
        text = self.globaluser
        response = rumps.Window("","Enter Your Steemit Name",text,"Save","Cancel",(200,100)).run()
        if response.clicked:
            tempuser = str(response.text)
            openAndWriteFile(tempuser)
            self.globaluser = globaluser = clicktext = tempuser
            if self.globaluser == '':
                self.title = 'Enter SteemName'
            else:    
                self.title = calcSteempower(self.globaluser,False)

    @rumps.clicked("Update Manually")
    def updatePower(self,_):
        self.title = calcSteempower(self.globaluser,False)
        
    @rumps.timer(10)
    def ticker(self, _):
        self.title = calcSteempower(self.globaluser,False)


if __name__ == "__main__":
    VotingPowerApp().run()


"""
This is not yet working
def calcTime():
    if firstCalc == True or toFill != startFill:
        print("First Calc =" + firstCalc)
        print(toFill + " / " + startFill)
        startFill = toFill
        firstCalc = False
        timeStart = time.time()
    else:
        timeNow = time.time() - timeStart
        timeString = "|" + secondsToText(timeNow)
        print(timeString)
"""