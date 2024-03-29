#This script will be run multiple times to pull the data on a regular basis. Scraping some trusted source for politician stock trades.
#I can automate this via crontab or maybe something on Github. 

import gspread
import gspread_dataframe
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import os

#directory of the current script
script_dir = os.path.dirname(__file__)

scope = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

relative_path = "./sheets_credentials.json"
absolute_filepath = os.path.join(script_dir, relative_path)
creds = ServiceAccountCredentials.from_json_keyfile_name(absolute_filepath, scope)

urls = {'sandbox': "https://docs.google.com/spreadsheets/d/11Nj7g8Zr18ogDvQaeqvXNd03cvsV_7OhgQjVsZNShP4/edit#gid=0"}


def create_table(df: pd.DataFrame, sheet_url: str, sheet_index=0):
    client = gspread.authorize(creds)
    sheet = client.open_by_url(sheet_url)
    ws = sheet.get_worksheet(sheet_index)
    gspread_dataframe.set_with_dataframe(ws, df)
    return


def access_google_sheet(google_sheet_url: str, sheet_num: int = 0) -> pd.DataFrame:
    client = gspread.authorize(creds)
    sheet = client.open_by_url(google_sheet_url)
    party_candidates_sheet = sheet.get_worksheet(sheet_num)

    party_candidates_dict = party_candidates_sheet.get_all_records()
    return pd.DataFrame(party_candidates_dict)


if __name__=="__main__":
    pass