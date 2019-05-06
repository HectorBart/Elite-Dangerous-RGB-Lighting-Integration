# required modules
from ChromaPython import ChromaApp, ChromaAppInfo
import glob
import os
import config
import lifx
import chroma
import cue
import hue
import subprocess
from time import sleep
from tkinter import *
import psutil


###########################################################


# main function
def start():

    processName = "elitedangerous"

    while 1 > 0:
        for proc in psutil.process_iter():
            if processName.lower() not in proc.name().lower():
                print("ED running")
                
                #Label(main, text = "You can minimize this window...", bg = "#000000", fg = "#f07b05", font = ("sintony", 12)).pack()

                if config.chromaEnable:

                    # app info and creation (chroma)
                    info = ChromaAppInfo()
                    info.DeveloperName = 'Hector Robe'
                    info.DeveloperContact = 'hector.brobe@gmail.com'
                    info.Category = 'application'
                    info.SupportedDevices = ['keyboard']
                    info.Description = 'Reacts to events in Elite Dangerous'
                    info.Title = 'Elite Dangerous Sync'
                    app = ChromaApp(info)
                    print("Chroma App Started")
                else:
                    print("Chroma App Not Started")

            ###########################################################


                # lights

                def whiteBright():
                    print("white bright testing")
                    try:
                        lifx.whiteBright()
                    except:
                        print("Failed LIFX")
                    try:
                        chroma.whiteBright(app)
                    except:
                        print("Failed Chroma")
                    try:
                        cue.whiteBright()
                    except:
                        print("Failed Cue")
                    try:
                        hue.whiteBright()
                    except:
                        print("Failed Hue")
                    
                def whiteDim():

                    try:
                        lifx.whiteDim()
                    except:
                        print("Failed LIFX")
                    try:
                        chroma.whiteDim(app)
                    except:
                        print("Failed Chroma")
                    try:
                        cue.whiteDim()
                    except:
                        print("Failed Cue")
                    try:
                        hue.whiteDim()
                    except:
                        print("Failed Hue")

                # start as dim white
                whiteDim()
                    
                def orange():

                    try:
                        lifx.orange()
                    except:
                        print("Failed LIFX")
                    try:
                        chroma.orange(app)
                    except:
                        print("Failed Chroma")
                    try:
                        cue.orange()
                    except:
                        print("Failed Cue")
                    try:
                        hue.orange()
                    except:
                        print("Failed Hue")
                    
                def flashGreen():

                    try:
                        chroma.flashGreen(app)
                    except:
                        print("Failed Chroma")
                    try:
                        lifx.flashGreen()
                    except:
                        print("Failed LIFX")
                    try:
                        cue.flashGreen()
                    except:
                        print("Failed Cue")
                    try:
                        hue.flashGreen()
                    except:
                        print("Failed Hue")

                def flashRed():

                    # counter
                    a = 0

                    while a < 10:

                        try:
                            chroma.flashRed(app)
                        except:
                            print("Failed Chroma")
                        try:
                            lifx.flashRed()
                        except:
                            print("Failed LIFX")
                        try:
                            cue.flashRed()
                        except:
                            print("Failed Cue")
                        try:
                            hue.flashRed()
                        except:
                            print("Failed Hue")

                        # add to counter
                        a = a + 1

                    # default
                    try:
                        lifx.whiteDim()
                    except:
                            print("Failed LIFX")
                    try:
                        chroma.whiteDim(app)
                    except:
                            print("Failed Chroma")
                    try:
                        cue.whiteDim()
                    except:
                            print("Failed Cue")
                    try:
                        hue.whiteDim()
                    except:
                            print("Failed Hue")

                def flashYellow():

                    try:
                        chroma.flashYellow(app)
                    except:
                            print("Failed Chroma")
                    try:
                        lifx.flashYellow()
                    except:
                            print("Failed LIFX")
                    try:
                        cue.flashYellow()
                    except:
                            print("Failed Cue")
                    try:
                        hue.flashYellow()
                    except:
                            print("Failed Hue")
                    
                def flashBlue():

                    try:
                        chroma.flashBlue(app)
                    except:
                            print("Failed Chroma")
                    try:
                        lifx.flashBlue()
                    except:
                            print("Failed LIFX")
                    try:
                        cue.flashBlue()
                    except:
                            print("Failed Cue")
                    try:
                        hue.flashBlue()
                    except:
                            print("Failed Hue")

            ########################################################

                sleep(20)

                # get latest log
                list_of_files = glob.glob(config.logLocation)
                try:
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
                    dockedMusic2 = '"event":"Music", "MusicTrack":"Exploration"'
                    dockedMusic = '"event":"Music", "MusicTrack":"Starport"'
                    undocked = '"event":"Undocked"'
                    dockGranted = '"event":"DockingGranted"'
                    kill = '"event":"PVPKill"'
                    supercruiseEnter = '"event":"SupercruiseEntry"'
                    supercruiseExit = '"event":"SupercruiseExit"'
                    dockingMusic = '"event":"Music", "MusicTrack":"DockingComputer"'
                    shutdown = '"event":"Shutdown"'


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
                                if shieldOff in lastLine:

                                    orange()
                                    sleep(1)

                                elif docked in lastLine or dockedMusic in lastLine or shutdown in lastLine: # or dockedMusic2 in lastLine:

                                    whiteBright()

                                elif shieldOn in lastLine or undocked or dockingMusic in lastLine:

                                    whiteDim()

                                elif dockGranted in lastLine or kill in lastLine:

                                    flashGreen()

                                elif supercruiseEnter in lastLine:

                                    flashYellow()

                                elif supercruiseExit in lastLine:

                                    flashBlue()
                                    
                                elif underAttack in lastLine or hullDamage in lastLine or heatDamage in lastLine or heatWarning in lastLine:
                                    
                                    flashRed()

                        # does nothing
                        else:
                            pass

                except:
                    print("Please add your Elite Dangerous log file location to the config.py file before running")

            else:
                print("ED not running")


########################################################


# gui setup
main = Tk()

main.title("Elite Dangerous Light Sync")
main.geometry("700x500")
main.configure(background = "#000000")

# logo image
edlogo = PhotoImage(file = "assets\edlogo2.gif")

# gui
Label(main, text = "Elite Dangerous Light Sync", bg = "#000000", fg = "#f07b05", font = ("euro caps", 38)).pack()
Label(main, bg = "#000000").pack()
Label(main, text = "Created by Hector Robe", bg = "#000000", fg = "#f07b05", bd = "0", font = ("sintony", 12)).pack()
Label(main, bg = "#000000").pack()
Button(main, compound = LEFT, image = edlogo, borderwidth = 0, highlightthickness = 0, pady = 0, padx = 10, text = "Start Lighting", relief = SOLID, command = start, bg = "#f07b05", fg = "#ffffff", font = ("euro caps", 32)).pack()
Label(main, bg = "#000000").pack()

# gui setup
main.mainloop()


