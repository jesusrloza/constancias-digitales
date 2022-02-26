#!/usr/bin/env python3
import os 
from lib.entorno import rutaConstInd, rutaCSV
from lib.csv_lista import csv_a_lista

# Lista de diccionarios que respresenten cada fila del excel
rows = csv_a_lista(rutaCSV)

# Usar rows para fabricar lista de nuevos nombres a partir de cada fila
nuevos_nombres = [
    "{:04d}_C{}F{:03d}R{:03d}.pdf".format(
        int(row["Global"]),row["Año"],int(row["Foja"]),int(row["No."]))
    for row in rows
]

# Lista ordenada de nombres de archivos PDF individuales
# os.listir NO entrega lista en orden alfabético, por eso se usa sorted()
pdfs = sorted(os.listdir(rutaConstInd))

# Iteramos por las dos listas para renombrar los archivos
for i in range(len(pdfs)):
    os.rename(
        os.path.join(rutaConstInd, pdfs[i]),
        os.path.join(rutaConstInd, nuevos_nombres[i])
    )

''' Columnas esperadas en el documento CSV para renombrar PDF's:
    | Global | Año | Foja | No. | 
    Notas: No. -> El número de registro del participante
'''
