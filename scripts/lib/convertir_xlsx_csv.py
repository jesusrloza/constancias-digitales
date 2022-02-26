#!/usr/bin/env python3
import pandas as pd
import os

def xlsx_a_csv(Excel, CSV, rutaAbsQR):

    ''' xlsx_a_csv(Excel, CSV, rutaAbsQR)
    (Excel a leer, CSV a escribir, directorio códigosQR)
    Excel & CSV ruta relativa, rutaAbsQR ruta absoluta.

    Lee el excel, crea un dataframe, añade columna 'QR' que señala al 
    archivo png correspondiente a cada renglón, escribe archivo CSV.
    '''

    # Si se ejecuta desde WSL cambia la ruta absoluta
    rutaQrWSL = rutaAbsQR.replace('/mnt/c/', 'C:/')

    # Construir un dataframe a partir de información en archivo xlsx
    df = pd.DataFrame(pd.read_excel(Excel))

    # Lista que toma la columna 'Global' y construye columna 'QR'
    columna_QR = [
        os.path.join('{}'.format(rutaQrWSL), '{:04d}.png'.format(int(g))).replace('/', '\\\\')
        for g in df['Global']
    ]  # Al escribir archivo csv '\' "escapa" el siguiente caracter, por eso se ponen 4

    # Incluir lista como una nueva columna
    df['QR'] = columna_QR

    # Escribir el archivo csv con la nueva información
    df.to_csv(CSV)
    return
