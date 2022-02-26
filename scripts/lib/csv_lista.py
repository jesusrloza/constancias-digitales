#!/usr/bin/env python3
import csv

def csv_a_lista(ruta_archivo_csv):
    """ Recibe una ruta a archivo csv, lo abre y regresa una lista
    de diccionarios. Un dict por cada fila """
    
    with open(ruta_archivo_csv) as participantes_csv:
        participantes_dict = csv.DictReader(participantes_csv)
        lista_participantes = list(participantes_dict)
        # lista_participantes:       [{fila1}, {fila2}, ...]
        # Cada dict = fila del csv:  {"Año":2020, "Foja":...}
    return lista_participantes

def csv_col_names(ruta_archivo_csv):
    """ Recibe una ruta a archivo csv, lo abre y regresa una lista
    con los nombres de cada columna """
    
    with open(ruta_archivo_csv) as participantes_csv:
        participantes_dict = csv.DictReader(participantes_csv)
        col_names = participantes_dict.fieldnames
    return col_names

