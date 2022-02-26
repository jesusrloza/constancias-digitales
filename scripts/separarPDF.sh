#!/usr/bin/sh

# Crear los directorios constancias e individuales en caso de que no existan
mkdir -p ../constancias/individuales

# Tomar archivo consolidado de constancias y separarlo en documentos individuales
pdfseparate ../constancias/constancias.pdf ../constancias/individuales/%04d.pdf

# Renombrar estos archivos con nombres genéricos, con información relevante
./renombrarPDF.py

