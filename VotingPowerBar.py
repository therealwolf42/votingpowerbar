import os
from datetime import datetime, tzinfo, timedelta
from decimal import Decimal
import rumps
import time
from steem import Steem


rumps.debug_mode(True)

def openAndWriteFile(tempuser):
    f = open("data.txt","w")
    f.write(tempuser)
    print("created file")
    f.close()

def readFile():
    if not os.path.isfile('./data.txt'):
        print("no file")
        openAndWriteFile("")

    f = open("data.txt")
    users = f.read().split("\n")
    f.close()
    return users

def getSteemPower(tempuser):
    return Steem().get_account(tempuser)['voting_power']

def getLastVoteTime(tempuser):
    return Steem().get_account(tempuser)['last_vote_time']

def dateToString(date_str):
        return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')

class simple_utc(tzinfo):
    def tzname(self,**kwargs):
        return "UTC"
    def utcoffset(self, dt):
        return timedelta(0)

class VotingPowerApp(rumps.App):
    
    globaluser = ''
    if globaluser == '':
        users = readFile()
        globaluser = users[0]

    if globaluser == '':
        clicktext = 'Name'
    else:
        clicktext = globaluser
    
    newCalc = True
    startFill = 0
    timeStart = 0
    timeNow = 0
    timeString = ""
    def __init__(self): 
        self.users = readFile()
        self.globaluser = globaluser = clicktext = self.users[0]
        if self.globaluser == '':
            titleValue = "Enter SteemName"
        else:
            titleValue = self.calcSteempower(self.globaluser)

        super(VotingPowerApp, self).__init__(titleValue)


    userLen = len(users)
    if userLen >= 1:
        @rumps.clicked("Change to " + users[0])
        def change1(self,_):
            self.globaluser = self.users[0]
            self.title = self.calcSteempower(self.globaluser)

    if userLen >= 2:
        @rumps.clicked("Change to " + users[1])
        def change2(self,_):
            self.globaluser = self.users[1]
            self.title = self.calcSteempower(self.globaluser)
    
    if userLen >= 3:
        @rumps.clicked("Change to " + users[2])
        def change3(self,_):
            self.globaluser = self.users[2]
            self.title = self.calcSteempower(self.globaluser)
    
    if userLen >= 4:
        @rumps.clicked("Change to " + users[3])
        def change(self,_):
            self.globaluser = self.users[3]
            self.title = self.calcSteempower(self.globaluser)
    
    if userLen >= 5:
        @rumps.clicked("Change to " + users[4])
        def change(self,_):
            self.globaluser = self.users[4]
            self.title = self.calcSteempower(self.globaluser)

    @rumps.clicked("Update Manually")
    def updatePower(self,_):
        self.title = self.calcSteempower(self.globaluser)
        
    @rumps.timer(5)
    def ticker(self, _):
        self.title = self.calcSteempower(self.globaluser)


    def calcSteempower(self,tempuser):
        lastVoteTime = dateToString(getLastVoteTime(tempuser))
        timeNow = dateToString(datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S"))
        delta = timeNow - lastVoteTime
        steempower = (getSteemPower(tempuser) + (10000 * delta.total_seconds() / 432000))/100
        if steempower <= 100:
            toFill = 100 - steempower
            perHour = 20/24
            timeToFill = toFill/perHour
            timeConst = "h"
            if timeToFill < 1:
                timeToFill = toFill/perHour/60
                timeConst = "m"
            else:
                hourToFill = Decimal(toFill / (20/24)).quantize(Decimal("0.1"))
                timeToFill = Decimal(timeToFill).quantize(Decimal("0.1"))
                stringFill = " (" + str(timeToFill) + timeConst + ")"
                steempower = Decimal(steempower).quantize(Decimal("0.1"))
        else:
            steempower = 100
            stringFill = ""
        

        return str(steempower) + "%" + stringFill 


if __name__ == "__main__":
    VotingPowerApp().run()

""" 
NOT YET WORKING:
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
                self.title = self.calcSteempower(self.globaluser)
"""
