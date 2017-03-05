"""part of program which will handle the monitoring"""

class WatchDog(object):
    """docstring for WatchDog"""
    def __init__(self):
        super(WatchDog, self).__init__()
        pass

    def check_power_status():
        output = subprocess.check_output("upower -i /org/freedesktop/UPower/devices/battery_BAT0",shell=True).split("\n")[11].split()[1]
        return output

    def logger():
        pass

    def capture():
        pass
