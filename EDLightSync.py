# required modules
from tkinter import *
import requests
from ChromaPython import ChromaApp, ChromaAppInfo, ChromaColor, Colors, ChromaGrid
import glob
import os

# access token (lifx)
token = "ACCESS TOKEN" # add your lifx access token here

# request header (lifx)
headers = {
    "Authorization": "Bearer %s" % token,
}

# app info and creation (chroma)
info = ChromaAppInfo()
info.DeveloperName = 'Hector Robe'
info.DeveloperContact = 'hector.brobe@gmail.com'
info.Category = 'application'
info.SupportedDevices = ['keyboard']
info.Description = 'Reacts to events in Elite Dangerous'
info.Title = 'Elite Dangerous Sync'
app = ChromaApp(info)


#############################################################

#counter
a = 0

# lights

def white():

    # chroma white
    app.Keyboard.setStatic(Colors.WHITE)

    # lifx white
    payload = {
        "power": "on",
        "color": "ffffff",
        "brightness": "1",
        "fast": "true",
    }

    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

def flashRed():

    # counter
    global a

    while a < 10:
        # chroma
        app.Keyboard.setStatic(Colors.RED)

        # lifx red on
        payload = {
            "power": "on",
            "color": "ff0000",
            "brightness": "1",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

        # lifx off
        payload = {
            "power": "off",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

        # add to counter
        a = a + 1

    #default
    white()


########################################################


# get latest log
list_of_files = glob.glob('DIRECTORY\*.log') # change directory to your ED journal directory
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)

# open latest log
currentLog = open(latest_file, 'r')

# defines events
music = '"event":"Music"'
underAttack = '"event":"UnderAttack", "Target":"You"'
hullDamage = '"event":"HullDamage"'
heatDamage = '"event":"HeatWarning"'
shieldOff = '"event":"ShieldState", "ShieldsUp":false'
shieldOn = '"event":"ShieldState", "ShieldsUp":true'

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
            if underAttack in lastLine or hullDamage in lastLine or heatDamage in lastLine:

                flashRed()

            elif shieldOff in lastLine:

                orange()

    # does nothing
    else:
        pass




