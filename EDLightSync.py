# required modules
from ChromaPython import ChromaApp, ChromaAppInfo
import glob
import os
import lifx
import chroma
import subprocess
import time

# app info and creation (chroma)
info = ChromaAppInfo()
info.DeveloperName = 'Hector Robe'
info.DeveloperContact = 'hector.brobe@gmail.com'
info.Category = 'application'
info.SupportedDevices = ['keyboard']
info.Description = 'Reacts to events in Elite Dangerous'
info.Title = 'Elite Dangerous Sync'
app = ChromaApp(info)


###########################################################


#counter
a = 0

# lights

def whiteBright():

    lifx.whiteBright()
    chroma.whiteBright(app)
    
def whiteDim():

    lifx.whiteDim()
    chroma.whiteDim(app)
    
def orange():

    lifx.orange()
    chroma.orange(app)
    
def flashGreen():

    chroma.flashGreen(app)
    lifx.flashGreen()

def flashRed():

    # counter
    global a

    while a < 10:

        chroma.flashRed(app)
        lifx.flashRed()

        # add to counter
        a = a + 1

    #default
    lifx.whiteDim()
    chroma.whiteDim(app)
    

########################################################


# get latest log
list_of_files = glob.glob('C:/Users/USERNAME/Saved Games/Frontier Developments/Elite Dangerous/*.log') # CHANGE THIS
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)

# open latest log
currentLog = open(latest_file, 'r')

# defines events
music = '"event":"Music", "MusicTrack":"NoTrack"'
underAttack = '"event":"UnderAttack", "Target":"You"'
hullDamage = '"event":"HullDamage"'
heatDamage = '"event":"HeatDamage"'
heatWarning = '"event":"HeatWarning"'
shieldOff = '"event":"ShieldState", "ShieldsUp":false'
shieldOn = '"event":"ShieldState", "ShieldsUp":true'
docked = '"event":"Docked"'
dockedMusic = '"event":"Music", "MusicTrack":"Starport"'
undocked = '"event":"Undocked"'
dockGranted = '"event":"DockingGranted"'
kill = '"event":"PVPKill"'


########################################################


# always watching events
while 0 < 1:

    # reads lines
    reader = currentLog.read().splitlines()

    # checks if any events exist
    if len(reader) != 0:

        # gets last line of log (most recent event)
        lastLine = reader[-1]

        # removes music from results
        if music not in lastLine:

            # prints last line of file
            print(lastLine)

            # checks for different events and runs functions
            if underAttack in lastLine or hullDamage in lastLine or heatDamage in lastLine or heatWarning in lastLine:

                flashRed()

            elif shieldOff in lastLine:

                orange()

            elif shieldOn in lastLine or undocked in lastLine:

                whiteDim()

            elif docked in lastLine or dockedMusic in lastLine:

                whiteBright()

            elif dockGranted in lastLine or kill in lastLine:

                flashGreen()

    # does nothing
    else:
        pass




