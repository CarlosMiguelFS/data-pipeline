import os
from os.path import join
import pandas as pd
from datetime import datetime, timedelta

date_initial = datetime.today()
date_final = date_initial + timedelta(days=7)

date_initial = date_initial.strftime('%Y-%m-%d')
date_final = date_final.strftime('%Y-%m-%d')
print(date_final)
location = 'Boston'

API_KEY = ''
URL_API = join(
    'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
    f'{location}/{date_initial}/{date_final}?unitGroup=metric&include=days&key={API_KEY}&contentType=csv'
)

dados = pd.read_csv(URL_API)
print(dados.head())

file_path = f'/home/carlosmiguel/Documentos/datapipeline/semana={date_initial}/'
os.mkdir(file_path)
dados.to_csv(file_path+'dados_brutos.csv')
dados[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path+'temperaturas.csv')
dados[['datetime', 'description', 'icon']].to_csv(file_path+'condicoes.csv')
