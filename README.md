# VotingPowerBar Python App for MacOSX
Python Script for displaying VotingPower % of specific Steem User in the MenuBar

Live Example
--------

![](https://github.com/therealwolf42/votingpowerbar/blob/master/votebar_action.gif)

User Example
--------
![](https://github.com/therealwolf42/votingpowerbar/blob/master/votebar_accounts.gif)

Required
--------
* Python 3 (https://www.python.org/downloads/)
* pip (should be part of python)
* Steem (https://github.com/steemit/steem-python)
* rumps (https://github.com/jaredks/rumps)


How-To
--------
1.) Open terminal and go to the folder for the bot.

2.) Install Python3 (from link)

3.) Install steem

        pip install -U steem
        
4.) Install rumps

    pip install rumps
    
5.) Start the script

    python votingpowerbar.py

If this doesn't work - try

    python3 votingpowerbar.py
    
You can also use py2app but currently only the alias mode works (this won't create a standalone to share - only on your local machine). 
Install py2app (e.g. via pip)first: (https://py2app.readthedocs.io/en/latest/install.html#installing-with-pip) and then:

      python setup.py py2app -A
    

Notes
--------
* If you want to change the usernames (max. 5 currently supported) just edit the data.txt directly.
* If you think that the timer might stop working you can 

1.) activate debug mode (just uncomment 'rumps.debug_mode(True)') 

2.) Update manually.

* If you have any custom wishes - let me know!


Known Bugs
--------
* py2app standalone build does not work / Works only via alias mode
* Editing Users in the APP while starting it from the console doesn't work and doesn't support multiple accounts. Thus I commented it out. Just edit in the text field and restart.
