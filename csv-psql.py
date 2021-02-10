#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import libreria

# Gestionamos los argumentos del script
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--fichero", help="Fichero a procesar")
parser.add_argument("-b", "--basedatos", help="Base de datos de trabajo" )
parser.add_argument("-m", "--host", help="Máquina dónde está la base de datos (por defecto localhost)" )
parser.add_argument("-p", "--puerto", help="Puerto de postgresql (por defecto 5432)" )
parser.add_argument("-u", "--user", help="Usuario de postgresql" )
parser.add_argument("-c", "--password", help="Contraseña del usuario de postgresql" )
parser.add_argument("-d", help="Se borra la tabla si esta existe", action="store_true" )
parser.add_argument("-k", help="Añade registros a la tabla si esta existe", action="store_true" )

args = parser.parse_args()

if not args.fichero:
    print('Necesitamos un fichero')
    quit()

print("El fichero es " + args.fichero)
fichero=args.fichero.strip()

if not args.basedatos:
    print("Necesitamos una base de datos")
    quit()

basedatos=args.basedatos.strip()

puerto=5432
host=''
usuario=''
password=''

if args.host:
    host = args.host

if args.puerto:
    puerto = args.puerto

if args.user:
    usuario= args.user.strip()

if args.password:
    password=args.password.strip()

# Comprobación del fichero de entrada de datos
try:
    f = open(fichero)
except:
    print('Error al abrir el fichero ' + fichero)
    quit()

n=0

#definimos objeto base y conectamos con la base de datos 
base=libreria.Base(basedatos, 'localhost', puerto, usuario, password)
b=base.conecta()
if b[:5] == 'Error':
    print(b)
    quit()

#nombre de la tabla igual que el nombre del fichero
tabla=fichero.split('.')[0]

#navegamos por el fichero
for linea in f:

    linea=linea[:len(linea)-1]
    if n == 0: 
        # Primera linea del fichero con los nombres y tio de campos
        campos=linea.split(",")
        if base.existeTabla(tabla) > 0:
            if args.d:
                t=base.borraTabla(tabla)
                print(t)
                t=base.creaTabla(tabla, campos)
                print(t)
            elif args.k:
                print('Añadiendo datos')
                t='      '
            else:
                print('tabla ' + tabla + ' ya existe')
                quit()

            if t[:5]=="Error":
                quit()
        else:
            t=base.creaTabla(tabla, campos)
            print(t)
    else:
        # Añadimos registros a la tabla
        valores=linea.split(",")       
        t=base.anadeRegistro(tabla, campos, valores)
        if t != None:
            print ('Error añadir registro: ' + t)
            
    n+=1

print('Registros añadidos')
f.close()
