# required modules
import requests
import config

if config.lifxEnable:

    # access token
    token = config.lifxKey

    # request header (lifx)
    headers = {
        "Authorization": "Bearer %s" % token,
    }

    # lights

    def whiteBright():

        # lifx white
        payload = {
            "power": "on",
            "color": "ffffff",
            "brightness": "1",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

    def whiteDim():

        # lifx white
        payload = {
            "power": "on",
            "color": "ffffff",
            "brightness": "0.3",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

    def orange():

        # lifx
        payload = {
            "power": "on",
            "color": "ff9900",
            "brightness": "1",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

    def flashGreen():

        # lifx green
        payload = {
            "power": "on",
            "color": "00ff00",
            "brightness": "1",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

        # default
        whiteDim()

    def flashRed():

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

    def flashYellow():

        # lifx yellow
        payload = {
            "power": "on",
            "color": "faff00",
            "brightness": "1",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

        # default
        whiteDim()

    def flashBlue():

        # lifx blue
        payload = {
            "power": "on",
            "color": "0000ff",
            "brightness": "1",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

        # default
        whiteDim()

    whiteBright()

else:
    print("LIFX Disabled")
