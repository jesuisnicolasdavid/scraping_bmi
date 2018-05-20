import subprocess
import pandas as pd
import requests
import io
from df2gspread import df2gspread as d2g


# def callSpyder():
#     cmdSpyder = '''curl -u 059c4862823346c0af120c8268931a40: https://app.scrapinghub.com/api/run.json -d project=308519 -d spider=www.leboncoin.fr_1'''
#     argsSpyder = cmdSpyder.split()
#     processSpyder = subprocess.Popen(argsSpyder, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     stdout, stderr = processSpyder.communicate()

def retrieveCSVfromScrapy():
    r = requests.get("https://storage.scrapinghub.com/items/308519/1/1?format=csv&fields=Contact,Description,Localisation,Prix,Mis_en_ligne,Origine,Pieces,Prix,Surface,Telephone2,Titre,Type_de_Bien&include_headers=1",
                auth=('059c4862823346c0af120c8268931a40',''))
    df = pd.read_csv(io.StringIO(r.text))   
    spreadsheet = './New Spreadsheet'
    wks_name = 'New Sheet Scrapy 2'
    d2g.upload(df, spreadsheet, wks_name)
  
   

if __name__ == '__main__':
   #callSpyder()
   retrieveCSVfromScrapy()
