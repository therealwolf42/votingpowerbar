# votingpowerbar
Python Script for displaying VotingPower % of specific Steem User in the MenuBar

Required
--------
* Python 3 (https://www.python.org/downloads/)
* Steem (https://github.com/steemit/steem-python)
* rumps (https://github.com/jaredks/rumps)


How-To
--------
Install Python3, Steem and rumps and then enter

    python votingpowerbar.py

If this doesn't work - try

    python3 votingpowerbar.py
    
You can also use py2app but currently only the alias mode works (this won't create a standalone to share). 
Install py2app e.g. via pip - first (https://py2app.readthedocs.io/en/latest/install.html#installing-with-pip) and then:

      pyton setup.py py2app -A
    

Notes
--------
* If you want to change the user name you can either enter the data.txt directly or simply click on "Change Name"


Known Bugs
--------
* py2app without alias mode doesn't work 
* Editing User in the APP while starting it from the console doesn't work. Just edit in the text field and restart.
* VotingPower has often a delay of a few hours - is a problem with the api (see: https://playground.steem.vc/#d5e8256d26f3f8ee59eb44d0b0df00c6)
* Ater some time the timer might stop working - try to "Update Manually" and see if that works or quit & restart
