#!/usr/bin/env python3
import os
from lib.entorno import rutaConstInd

nombres = sorted(os.listdir(rutaConstInd))

# os.listir NO entrega una lista en orden alfabético
# usar junto a sorted() para preservar el orden

años  = [str(x) for x in range(2017,2021)]
fojas = [str(x).zfill(3) for x in range(1,501)]

for año in años:
    #Si no existe una carpeta de año, se crea
    rutaAño = os.path.join(rutaConstInd, 'Año_' + año)
    if not os.path.exists(rutaAño): os.mkdir(rutaAño)

    for foja in fojas:
        #Si no existe una carpeta de foja, se crea
        rutaFoja = os.path.join(rutaAño, 'Foja_' + foja)
        if not os.path.exists(rutaFoja): os.mkdir(rutaFoja)

        for nombre in nombres:
            rutaArchivo = os.path.join(rutaConstInd, nombre)
            if "C{}F{}".format(año, foja) in nombre:
                os.rename(rutaArchivo, rutaFoja + nombre)

