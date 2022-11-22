import psutil

class Addon():
    name = 'CPU temperature'
    icon = 'mdi:temperature-celsius'
    unit = '°C'

    def getInfo(self):
        temperatures = psutil.sensors_temperatures(fahrenheit=False)

        return temperatures['coretemp'][0].current
