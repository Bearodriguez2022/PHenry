import pandas as pd
import numpy as np

def agregar_id(df):
    if df.name == 'amazon':
        df['NuevoId'] = 'a'+ df['show_id']
        df['plataforma'] = 'amazon'
    if df.name == 'disney':
        df['NuevoId'] = 'd'+ df['show_id']
        df['plataforma'] = 'disney'
    if df.name == 'hulu':
        df['NuevoId'] = 'h'+ df['show_id']
        df['plataforma'] = 'netfix'
    if df.name == 'hulu':
        df['NuevoId'] = 'n'+ df['show_id']
        df['plataforma'] = 'netfix'


def reeplace_nan(df_streaming):
    df_streaming['rating'] = df_streaming['rating'].fillna('G')

def minusculas(df_streaming):
    
    df_streaming = df_streaming.apply(lambda x: x.astype(str).str.lower() if x.dtype == 'object' else x)

def fecha(df_streaming, column):
    df_streaming['date_added'] = pd.to_datetime(df_streaming['date_added'])

def split_duration(df_streaming):
    #creo los dos campos solicitados , separando duration para darle los valores correspondientes
    df_streaming[['duration_int', 'duration_type']] = df_streaming['duration'].str.split(' ', expand=True)

#leo todos los datos
amazon = pd.read_csv(r'F:\usuarios\alumno\Escritorio\Streaming\PI-BBDD\amazon_prime_titles.csv')
amazon.name = 'amazon'#el punto name sirve para cuando llamamos el df_streaming mas arriba
disney = pd.read_csv(r'F:\usuarios\alumno\Escritorio\Streaming\PI-BBDD\disney_plus_titles.csv')
disney.name = 'disney'
hulu = pd.read_csv(r'F:\usuarios\alumno\Escritorio\Streaming\PI-BBDD\hulu_titles.csv')
hulu.name = 'hulu'
netflix = pd.read_csv(r'F:\usuarios\alumno\Escritorio\Streaming\PI-BBDD\netflix_titles.csv')
netflix.name = 'netflix'
streaming =  pd.concat([amazon, disney, hulu,netflix])
streaming.name = 'df_streaming'

r1 = pd.read_csv(r'F:\usuarios\alumno\Escritorio\Streaming\PI-BBDD\ratings\1.csv')
r2 = pd.read_csv(r'F:\usuarios\alumno\Escritorio\Streaming\PI-BBDD\ratings\2.csv')
r3= pd.read_csv(r'F:\usuarios\alumno\Escritorio\Streaming\PI-BBDD\ratings\3.csv')
r4 = pd.read_csv(r'F:\usuarios\alumno\Escritorio\Streaming\PI-BBDD\ratings\4.csv')
r5 = pd.read_csv(r'F:\usuarios\alumno\Escritorio\Streaming\PI-BBDD\ratings\5.csv')
r6 = pd.read_csv(r'F:\usuarios\alumno\Escritorio\Streaming\PI-BBDD\ratings\6.csv')
r7 = pd.read_csv(r'F:\usuarios\alumno\Escritorio\Streaming\PI-BBDD\ratings\7.csv')
r8 = pd.read_csv(r'F:\usuarios\alumno\Escritorio\Streaming\PI-BBDD\ratings\8.csv')

#pruebo funciones
agregar_id(amazon)
reeplace_nan(df_streaming= streaming)
minusculas(df_streaming= streaming)
fecha(df_streaming= streaming, column='date_added')
split_duration(df_streaming= streaming)

rating = pd.concat([r1,r2,r3,r4,r5,r6,r7,r8])
streaming.to_csv('streaming.csv',index= False)#convierto en csv

print('ETL Terminado')

