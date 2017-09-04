from setuptools import setup

APP = ['VotingPowerBar.py']
DATA_FILES = ['data.txt']
OPTIONS = {
    'argv_emulation': True,
    'iconfile':'steem.icns',
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps','steem'],
}

setup(
    app=APP,
    name='VotingPowerBar',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)