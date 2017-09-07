# VotingPowerBar Python App for MacOSX
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
    
You can also use py2app but currently only the alias mode works (this won't create a standalone to share - only on your local machine). 
Install py2app (e.g. via pip)first: (https://py2app.readthedocs.io/en/latest/install.html#installing-with-pip) and then:

      pyton setup.py py2app -A
    

Notes
--------
* If you want to change the user names (max. 5 currently supported) you can either enter the data.txt directly or simply click on "Change Name". However if you start from the console - you have to edit it in data.txt
* If you think that the timer might stop working you can 
1.) activate debug mode (just uncomment 'rumps.debug_mode(True)') 
2.) Update manually.
* If you have any custom wishes - let me know!


Known Bugs
--------
* py2app standalone build does not work / Works only via alias mode
* Editing Users in the APP while starting it from the console doesn't work. Thus I commented it out. Just edit in the text field and restart.
