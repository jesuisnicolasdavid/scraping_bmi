import gspread
import pandas as pd
import requests
import io
from gspread_dataframe import get_as_dataframe, set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials


# def callSpyder():
#     cmdSpyder = '''curl -u 059c4862823346c0af120c8268931a40: https://app.scrapinghub.com/api/run.json -d project=308519 -d spider=www.leboncoin.fr_1'''
#     argsSpyder = cmdSpyder.split()
#     processSpyder = subprocess.Popen(argsSpyder, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     stdout, stderr = processSpyder.communicate()

def retrieveCSVfromScrapy():
    r = requests.get("https://storage.scrapinghub.com/items/308519/1/1?format=csv&fields=Contact,Description,Localisation,Prix,Mis_en_ligne,Origine,Pieces,Prix,Surface,Telephone2,Titre,Type_de_Bien&include_headers=1",
                    auth=('059c4862823346c0af120c8268931a40',''))
    df = pd.read_csv(io.StringIO(r.text))
    df = df.fillna(value="--------")
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('script/bmibmi-67d3f1f00f49.json', scope)
    gc = gspread.authorize(credentials)
    sheet = gc.open_by_key("13zRKY5reR-AQt_CE4uNWCcSdfIoRKgAogdg05ejfLNI")
    worksheet = sheet.get_worksheet(0)
    set_with_dataframe(worksheet, df)
  

if __name__ == '__main__':
   #callSpyder()
   retrieveCSVfromScrapy()
