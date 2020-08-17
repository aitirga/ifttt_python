import requests, os, time, sys
from dotenv import load_dotenv, find_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from ifttt_python.utils import get_root_path
import os.path
from gspread import Client
import pandas as pd
from ifttt_python.source import IftttController


def add_sheet():
    requests.post(f"https://maker.ifttt.com/trigger/location_test_trigger/with/key/{os.getenv('IFTTT_KEY')}", data={"value1": 1})


if __name__ == "__main__":
    ifttt_controller = IftttController()
    i = 0
    while 1:
        print(ifttt_controller.get_google_sheet(sheet_name="aitor-location"))
        ifttt_controller.trigger(trigger_name="location_test_trigger", data={"value1": i})
        i += 1





