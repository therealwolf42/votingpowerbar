import os
import rumps
import time
from steem import Steem
from decimal import Decimal

rumps.debug_mode(True)

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




class VotingPowerApp(rumps.App):
    globaluser = ''
    clicktext = 'Name'
    newCalc = True
    startFill = 0
    timeStart = 0
    timeNow = 0
    timeString = ""
    def __init__(self): 
        self.globaluser = globaluser = clicktext = readFile()
        if not self.globaluser:
            print("empty" + self.globaluser)
            clicktext = "SteemUser"
            titleValue = "Enter SteemName"
        else:
            titleValue = self.calcSteempower(self.globaluser,True)
            
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
                self.title = self.calcSteempower(self.globaluser,False)


    @rumps.clicked("Update Manually")
    def updatePower(self,_):
        self.title = self.calcSteempower(self.globaluser,False)
        
    @rumps.timer(5)
    def ticker(self, _):
        self.title = self.calcSteempower(self.globaluser,False)


    def calcSteempower(self,tempuser,boolInit):
        toFill = 100 - getSteemPower(tempuser)
        secToFill = Decimal(toFill / (20/24/60/60)).quantize(Decimal("0.1"))   
        minToFill = Decimal(toFill / (20/24/60)).quantize(Decimal("0.1"))
        hourToFill = Decimal(toFill / (20/24)).quantize(Decimal("0.1"))
        dayToFill = Decimal(toFill / 20).quantize(Decimal("0.1"))

        print(toFill)
        timeString = ""
        print(self.startFill)
        if self.newCalc == True or toFill != self.startFill:
            print("New Calc")
            self.startFill = toFill
            self.newCalc = False
            self.timeStart = time.time()
        else:
            timeNow = time.time() - self.timeStart
            print(timeNow)
            timeString = "|" + str(Decimal(timeNow / 60 / 60).quantize(Decimal("0.1"))) + "h|" +  str(Decimal(timeNow / 60 * (20/24/60)).quantize(Decimal("0.01"))) + "%"
            print(timeString)        
            
        
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
            hourToFill = Decimal(toFill / (20/24)).quantize(Decimal("0.1"))
            stringFill = "~" + str(hourToFill) + "h"

        return str(getSteemPower(tempuser)) + "% (" + stringFill + timeString + ")" 



if __name__ == "__main__":
    VotingPowerApp().run()
