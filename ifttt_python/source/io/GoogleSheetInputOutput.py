from ifttt_python.source.io import BaseInputOutput
import logging
import gspread
from gspread import Client
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from pathlib import Path
logger = logging.getLogger(__name__)


class GoogleSheetInputOutput(BaseInputOutput):
    def __init__(self):
        """Automatically authoentifies the system"""
        self.google_service = self.auth_google()

    @staticmethod
    def auth_google(token_file="client_secret.json"):
        logger.info("Authentificating on Google Drive")
        """Authorizes google sheet"""
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']

        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            Path.cwd() / token_file, scope)  # Your json file here
        gc = gspread.authorize(credentials)
        return gc

    def get_spreadsheet(self, sheet_name):
        wks = self.google_service.open(sheet_name).sheet1
        data = wks.get_all_values()
        headers = data.pop(0)
        self.data = pd.DataFrame(data, columns=headers)
        return self.data

    @property
    def spreedsheet(self):
        self.get_spreadsheet()
        return self.data