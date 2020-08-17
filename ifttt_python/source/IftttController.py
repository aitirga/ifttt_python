from ifttt_python.config import config
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
from ifttt_python.utils import *
import requests
from ifttt_python.source.io import *
import logging

logger = logging.getLogger(__name__)
class IftttController(object):
    def __init__(self):
        load_dotenv(find_dotenv())
        self.key = os.getenv("IFTTT_KEY")

    def trigger(self, trigger_name, data={}):
        requests.post(f"https://maker.ifttt.com/trigger/{trigger_name}/with/key/{self.key}", data=data)
        logger.info(f"Triggered {trigger_name} using {data} data")

    def get_google_sheet(self, sheet_name):
        logger.info(f"Requesting data from {sheet_name}")
        if not config.globals.google_authentification:
            self.google_sheet = GoogleSheetInputOutput()
            config.globals.google_authentification = True
        return self.google_sheet.get_spreadsheet(sheet_name=sheet_name)