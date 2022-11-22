from os import popen


class Addon():
    name = 'Idle'
    icon = 'mdi:timer-sand'
    unit = 'sec'

    def getInfo(self):
        milliseconds_string = popen("xprintidle").read()
        return int(milliseconds_string)/1000
