from os import popen


class Addon():
    name = 'GPU temperature'
    icon = 'mdi:temperature-celsius'
    unit = '°C'

    def getInfo(self):
        return popen("nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits").read()
