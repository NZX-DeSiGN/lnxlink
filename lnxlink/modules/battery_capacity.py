from pathlib import Path

class Addon():
    name = 'Battery capacity'
    icon = 'mdi:battery'
    unit = '%'

    def getInfo(self):
        return Path('/sys/class/power_supply/BAT0/capacity').read_text()
