import requests
from idle_time import IdleMonitor
import time
import sys


def studio_lights_on():
    requests.post("https://maker.ifttt.com/trigger/studio_lights_on/with/key/m5jCtuQgMIcmNil_xxoNN")


def studio_lights_off():
    requests.post("https://maker.ifttt.com/trigger/studio_lights_off/with/key/m5jCtuQgMIcmNil_xxoNN")


if __name__ == "__main__":
    arg = sys.argv
    monitor = IdleMonitor.get_monitor()
    monitor.get_idle_time()
    try:
        max_idle_time = float(arg[1])
    except IndexError:
        max_idle_time = 30.0
    current_status = False
    while 1:
        time.sleep(1.0)
        if monitor.get_idle_time() > max_idle_time and current_status == True:
            studio_lights_off()
            current_status = False
            print("send OFF")
        if monitor.get_idle_time() < max_idle_time and current_status == False:
            studio_lights_on()
            current_status = True
            print("send ON")