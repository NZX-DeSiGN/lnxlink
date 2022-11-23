from pathlib import Path

class Addon():
    name = 'Battery level'
    icon = 'mdi:battery'
    unit = None

    def getInfo(self):
        return Path('/sys/class/power_supply/BAT0/capacity_level').read_text()
