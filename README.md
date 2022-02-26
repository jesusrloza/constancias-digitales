# Constancias Digitales

Proyecto para elaboración de constancias digitales en dependencias de gobierno que imparten cursos, talleres y conferencias.

---

## Archivo de constancia

* Constancia.docx -> El diseño actualizado de constancia en formato editable

## docs

* Manual para elaboración de Constancias Digitales 
* Explicación de OpenSSL y Qrencode

## códigosQR

Archivos PNG de cada código QR generado en el script **qrGen.py**.

Formato a 4 dígitos. Ej: 0001.png 

## constancias

* constancias.pdf -> Tiraje de constancias resultado de la combinación de correspondencia.
* individuales/   -> Directorio donde se separan y renombran los archivos PDF individuales en el script **separarPDF.sh**.

## datos

* "Base de Datos Participantes - 2021.xlsx" -> Base de datos de participantes.
* "participantes.csv"                       -> Archivo fabricado al ejecutar **qrGen.py**.

## scripts

* lib/            -> Directorio que contiene scripts con funciones y variables necesarias para elaboración de constancias.
* wsl_win/        -> Directorio con scripts para configuración inicial de Windows y de Ubuntu en WSL2.
* organizarPDF.py -> Script para organizar las constancias por año y foja. 
* qrGen.py        -> Script para fabricar archivo CSV y códigos QR.
* renombrarPDF.py -> Script para cambiar nombre de los archivos PDF individuales.
* separarPDF.sh   -> Script para separar consolidado de constancias en archivos individuales y ejecuta renombrarPDF.py
