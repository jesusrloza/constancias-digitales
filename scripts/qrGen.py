#!/usr/bin/env python3
import sys, subprocess
from lib.csv_lista import csv_a_lista
from lib.entorno import revisar_entorno, rutaCSV, rutaQR

# Si no están presentes los archivos necesarios se interrumpe el programa
if revisar_entorno():
    print("Imposible continuar")
    sys.exit()

# Fabricar lista de diccionarios que respresenten cada fila del excel
rows = csv_a_lista(rutaCSV)

# Iterar por esta lista de filas
for row in rows:
    # Limpieza de sellos digitales con apóstrofe
    if "'" in row['Constancia']: row['Constancia'] = row['Constancia'][1:]
    
    # Asignación de nombre al archivo.png del código (A 4 dígitos)
    qrname = "{:04d}".format(int(row['Global']))

    # Fabricación de texto a codificar tomando variables de cada fila
    if '1.0' in row['Duración en horas']:
        row["Duración en horas"] = int(row["Duración en horas"])
        hr_hrs = 'hora'        
    else:
        hr_hrs = 'horas'

    qrstring = (
        "° Dirección de Profesionalización, SFA Michoacán {} | Foja {} - {} ({} {}) | Participante: {} | ID: {}".format(
            row['Año'], row["Foja"], row["Curso"], row["Duración en horas"], hr_hrs, row["Participante"], row["Constancia"]
        )
    )
    
    # Se usa "qrencode" para fabricar un código por fila
    subprocess.run(["qrencode", "-o", "{}/{}.png".format(rutaQR, qrname), "{}".format(qrstring)])

''' Columnas esperadas en el documento CSV para generar códigosQR:
    | Global | Año | Foja | Curso | Duración en horas |
    | Participante | Constancia |
'''
