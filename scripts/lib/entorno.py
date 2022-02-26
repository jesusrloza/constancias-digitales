#!/usr/bin/env python3
import os
from lib.convertir_xlsx_csv import xlsx_a_csv
from lib.csv_lista import csv_col_names

# Ruta a distintos elementos necesarios para la elaboración de constancias
inicio = ".."
rutaQR =    os.path.join(inicio, "códigosQR")
rutaAbsQR = os.path.abspath(rutaQR)
rutaDatos = os.path.join(inicio, "datos")
rutaExcel = os.path.join(rutaDatos, "Base de Datos Participantes - 2021.xlsx")
rutaCSV =   os.path.join(rutaDatos, "participantes.csv")
rutaConstInd = os.path.join(inicio, "constancias", "individuales")

def revisar_entorno():
    ''' Valida la existencia de directorios y archivos requeridos o los crea.
    De no ser posible continuar se notifica en terminal y termina ejecución.
    '''

    if not os.path.exists(rutaQR): os.mkdir(rutaQR)
    if not os.path.exists(rutaDatos): os.mkdir(rutaDatos)

    if not os.path.exists(rutaCSV):
        print("No se encontró {}".format(rutaCSV))

        if not os.path.exists(rutaExcel):
            # No existen csv ni xlsx, no se puede continuar
            print("No se encontró {}".format(rutaExcel))
            return 1

        # Existe el excel pero no el csv
        print("Fabricando archivo csv a partir del xlsx")
        xlsx_a_csv(rutaExcel, rutaCSV, rutaAbsQR)
    
    # Revisar columnas requisito contra las encontradas en el csv
    columnas_csv = csv_col_names(rutaCSV)
    columnas_requisito = [
        'Global', 'Año', 'Foja', 'No.', 'Curso', 'Duración en horas',
        'Participante', 'Constancia', 'QR'
    ] # Necesarias para generar códigos qr y renombrar PDFs
    
    # Si no están todas se reporta y termina la ejecución
    if not all(elemento in columnas_csv for elemento in columnas_requisito):
        print("Falta alguna de las siguientes columnas: {}.".format(
            ', '.join(columnas_requisito)
        ))
        return 1

    print("Entorno revisado con éxito, se puede continuar")
    return
