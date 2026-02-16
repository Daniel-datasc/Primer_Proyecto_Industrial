import boto3
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from io import StringIO

# 1. Configuracion de Rutas y Nombres
BUCKET_NAME = 'datavergencia-industrial-datos'
FILE_NAME = 'prueba_bloqueo.csv'
GOOGLE_SHEET_NAME = 'Reporte_Proyecto_Scrap'
KEY_FILE = 'Himitsu.json'

def ejecutar_integracion():
    try:
        # --- PARTE A: LECTURA DESDE AWS S3 ---
        s3 = boto3.client('s3')
        obj = s3.get_object(Bucket=BUCKET_NAME, Key=FILE_NAME)
        df = pd.read_csv(StringIO(obj['Body'].read().decode('utf-8')))
        
        # --- PARTE B: PROCESAMIENTO (Opcional - Limpieza basica) ---
        # Convertimos los datos a una lista para enviarlos a Google
        datos_para_hoja = [df.columns.values.tolist()] + df.values.tolist()

        # --- PARTE C: ENVIO A GOOGLE SHEETS ---
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(KEY_FILE, scope)
        client = gspread.authorize(creds)
        
        sheet = client.open(GOOGLE_SHEET_NAME).sheet1
        
        # Limpiamos la hoja antes de escribir los nuevos datos
        sheet.clear()
        
        # Actualizamos la hoja con el contenido del CSV
        sheet.update('A1', datos_para_hoja)
        
        print("Integracion finalizada: Datos de S3 transferidos exitosamente a Google Sheets.")

    except Exception as e:
        print(f"Error en la ejecucion: {e}")

if __name__ == "__main__":
    ejecutar_integracion()
