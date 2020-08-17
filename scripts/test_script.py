import requests
from idle_time import IdleMonitor
import time
import sys
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import os
from ifttt_python.config import config
import logging

logger = logging.getLogger(__name__)

def studio_lights_on():
    requests.post(f"https://maker.ifttt.com/trigger/studio_lights_on/with/key/{os.getenv('IFTTT_KEY')}")

def studio_lights_off():
    requests.post(f"https://maker.ifttt.com/trigger/studio_lights_off/with/key/{os.getenv('IFTTT_KEY')}")


if __name__ == "__main__":
    arg = sys.argv
    monitor = IdleMonitor.get_monitor()
    monitor.get_idle_time()
    load_dotenv(find_dotenv())
    try:
        max_idle_time = float(arg[1])
    except IndexError:
        max_idle_time = 90.0
    current_status = False
    while 1:
        time.sleep(1.0)
        if monitor.get_idle_time() > max_idle_time and current_status:
            studio_lights_off()
            current_status = False
            logger.info("Sent lights OFF message")
        if monitor.get_idle_time() < max_idle_time and not current_status:
            studio_lights_on()
            current_status = True
            logger.info("Sent lights ON message")
