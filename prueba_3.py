# -*- coding: utf-8 -*-
"""prueba_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ThonCzuy6-gezW9C80TXaQQCw8INlzgH
"""

import random
from datetime import datetime
#Variables
patentes = []
tipo_vh = []
marcas = []
precios = []
fecha_registro_vh = []
nombre_dueños = []
apellido_dueños = []
multa_montos = []
multa_fechas = []
opc_menu = ""
patente = ""
marca = ""
precio = ""
tipo_vehiculo = ""
multa_fecha = ""
multa_monto = ""
fecha_registro = ""
nombre_dueño = ""
apellido_dueño = ""
posicion = ""
nom_pat = ""
opc_emi = ""
opc_vig = ""
precio_vig = 0
precio_emi = 0
#codigo
while True:

  print('''
     __________________________
    |Bienvenido a Auto Seguro  |
    |--------------------------|
    | 1) Grabar datos          |
    |--------------------------|
    | 2) Buscar datos          |
    |--------------------------|
    | 3) Imprimir certificados |
    |--------------------------|
    | 4) Salir                 |
    |__________________________|

      ''')
  opc_menu = input(" Elija una opcion ")
  while not opc_menu.isnumeric() or int(opc_menu) <1 or int(opc_menu) >4:
    print(" Solamente se aceptan caracteres numericos con valor maximo 4 vuelva a introducir la opcion ")
    opc_menu = input(" Elija una opcion ")
  if int(opc_menu) == 1:
    print(" introduzca sus datos")

    tipo_vehiculo = input(' Ingrese el tipo de vehiculo que desea (automovil, motocicleta, bus): ')
    while tipo_vehiculo.lower() not in ['automovil', 'motocicleta', 'bus']:
      print('Tipo de vehiculo invalido')
      tipo_vehiculo = input(' Ingrese el tipo de vehiculo que desea (automovil, motocicleta, bus): ')

    if tipo_vehiculo.lower() == 'automovil':
      print('El tipo de vehiculo ingresado es Automóvil')

    elif tipo_vehiculo.lower() == 'motocicleta':
      print('El tipo de vehiculo ingresado es Motocicleta')

    elif tipo_vehiculo.lower() == 'bus':
      print('El tipo de vehiculo ingresado es Bus')

    patente = input(" introduzca su patente ")
    while not patente.isalnum() or len(patente) != 6:
      print(" introducir la patente sin giones ni espacios y deben ser 6 caracteres ")
      patente = input(" introduzca su patente ")

    marca = input(" introduzca la marca de su vehiculo ")
    while not len(marca) >= 2 or len(marca) >= 15:
      print(" introducir la marca en un minimo de 2 caracteres y un maximo de 15")
      marca = input(" introduzca la marca de su vehiculo ")

    precio = input(" Introduzca el precio de su vehiculo ")
    while not precio.isnumeric() or int(precio) < 5000000:
      print(" El precio debe ser introducido con numero y debe ser mayor a 5.000.000 ")
      precio = input(" Introduzca el precio de su vehiculo ")

    multa_monto =  input(" Introduzca el monto de la multa ")
    while not multa_monto.isnumeric():
      print(" Solamente se aceptan caracteres numericos ")
      multa_monto = input(" Introduzca el monto de la multa ")

    multa_fecha = input("Ingrese la fecha de la multa del vehículo (formato: DD/MM/AAAA): ")
    try:
        multa_fecha = datetime.strptime(multa_fecha, "%d/%m/%Y").date()
        print(f"La fecha de multa del vehículo es: {multa_fecha}")
    except ValueError:
        print("Formato de fecha incorrecto. Asegúrese de ingresar la fecha en el formato indicado.")
        multa_fecha = input("Ingrese la fecha de registro del vehículo (formato: DD/MM/AAAA): ")

    fecha_registro = input("Ingrese la fecha de registro del vehículo (formato: DD/MM/AAAA): ")
    try:
        fecha_registro = datetime.strptime(fecha_registro, "%d/%m/%Y").date()
        print(f"La fecha de registro del vehículo es: {fecha_registro}")
    except ValueError:
        print("Formato de fecha incorrecto. Asegúrese de ingresar la fecha en el formato indicado.")
    nombre_dueño = input(" Introduzca su nombre ")
    while not nombre_dueño.isalpha():
      print(" Solamente se aceptan letras ")
      nombre_dueño = input(" Introduzca su nombre ")

    apellido_dueño = input(" Introduzca su apellido ")
    while not apellido_dueño.isalpha():
      print(" Solamente se aceptan letras ")
      apellido_dueño = input(" Introduzca su apellido ")

    opc_vig = input(" ¿Tiene anotaciones vigentes? responder con un si/no ")
    while not opc_vig.isalpha():
      print("Responder con un si/no")
    if opc_vig.lower() == "si":
      print("se ha guardado su respuesta")
      precio_vig = random.randint(1500, 3500)
    if opc_vig.lower() == "no":
      print("se ha guardado su respuesta")
      pass
    else:
      print("Responder con un si/no")

    opc_emi = input(" ¿Tiene certificado de Emisiones? Responder con un si/no")
    while not opc_emi.isalpha():
      print("Responder con un si/no")
    if opc_emi.lower() == "si":
      print("se ha guardado su respuesta")
      precio_emi = random.randint(1500, 3500)
    if opc_emi.lower() == "no":
      print("se ha guardado su respuesta")
      pass
    else:
      print("Responder con un si/no")

    patente = patente.lower()
    marca = marca.lower()
    precio = precio.lower()
    nombre_dueño = nombre_dueño.lower()
    apellido_dueño = apellido_dueño.lower()
    multa_monto = multa_monto.lower()

    tipo_vh.append(tipo_vehiculo)
    patentes.append(patente)
    marcas.append(marca)
    precios.append(precio)
    multa_montos.append(multa_monto)
    multa_fechas.append(multa_fecha)
    fecha_registro_vh.append(fecha_registro)
    nombre_dueños.append(nombre_dueño)
    apellido_dueños.append(apellido_dueño)

  if int(opc_menu) == 2:
    for nom_pat in patentes:
      nom_pat = input(" Introduzca su patente para buscar ")
      while not nom_pat in patentes:
        print(" No se encuentra la patente")
        nom_pat = input(" Introduzca su patente para buscar ")
      posicion = patentes.index(nom_pat)
      print(f'''
      Tipo de vehiculo
      {tipo_vh[posicion]}

      Patente
      {patentes[posicion]}

      Marca
      {marcas[posicion]}

      precio del vehiculo
      ${precios[posicion]}

      Precio de la multa
      ${multa_montos[posicion]}

      Fecha de la multa
      {multa_fechas[posicion]}

      Fecha de registro del vehiculo
      {fecha_registro_vh[posicion]}

      Nombre del dueño
      {nombre_dueños[posicion]}

      Apellido del dueño
      {apellido_dueños[posicion]}

      ''')
      break
  elif int(opc_menu) == 3:
    for nom_pat in patentes:
      nom_pat = input(" Introduzca su patente para imprimir su certificado ")
      while not nom_pat.isalnum() or len(nom_pat) != 6:
        print(" introducir la patente sin giones ni espacios y deben ser 6 caracteres ")
        nom_pat = input(" Introduzca su patente para imprimir su certificado  ")
      while not nom_pat in patentes:
        print(" No se encuentra la patente")
        nom_pat = input(" Introduzca su patente para imprimir su certificado  ")
      posicion = patentes.index(nom_pat)
      break
    print('''
     ______________________________
    |        Certificados          |
    |------------------------------|
    | 1) Emisión de contaminantes  |
    |------------------------------|
    | 2) Anotaciones vigentes      |
    |------------------------------|
    | 3) Multas                    |
    |______________________________|
    ''')
    opc_cer = input(" Elija el certificado que desea imprimir ")
    while not opc_cer.isnumeric() or int(opc_cer) > 3 or int(opc_cer) < 1:
      print(" El valor ingresado debe ser numerico con valor minimo 1 y máximo 3")
      opc_cer = input(" Elija el certificado que desea imprimir ")
    if int(opc_cer) == 1:
      print(f'''
      ____________________________
     |       Certificado de       |
     |   Emisión de contaminantes |
     |----------------------------|
     |           Patente          |
     |         {patentes[posicion]}
     |----------------------------|
     | Nombre           Apellido  |
     |{nombre_dueños[posicion]}           {apellido_dueños[posicion]}
     |----------------------------|
     |          precio            |
     |         ${precio_emi}
     |____________________________|

            ''')
    if int(opc_cer) == 2:
      print(f'''
      ____________________________
     |       Certificado de       |
     |     Anotaciones Vigentes   |
     |----------------------------|
     |           Patente          |
     |         {patentes[posicion]}
     |----------------------------|
     | Nombre           Apellido  |
     |{nombre_dueños[posicion]}           {apellido_dueños[posicion]}  |
     |----------------------------|
     |           Precio           |
     |         ${precio_vig}
     |____________________________|

            ''')
    if int(opc_cer) == 3:
      print(f'''
      ____________________________
     |       Certificado de       |
     |           Multas           |
     |----------------------------|
     |           Patente          |
     |         {patentes[posicion]}
     |----------------------------|
     | Nombre           Apellido  |
     |{nombre_dueños[posicion]}           {apellido_dueños[posicion]}
     |----------------------------|
     |           Multa            |
     |         ${multa_montos[posicion]}
     |         {multa_fechas[posicion]}
     |____________________________|

            ''')

  elif int(opc_menu) == 4:
    print('''
     ___________________________________________________________________________________
    | Usted esta saliendo del programa, muchas gracias por utilizar nuestros servicios. |
    |-----------------------------------------------------------------------------------|
    |                     Sebastian Matamoros y Javier Castro                           |
    |                                version 1.5                                        |
    |___________________________________________________________________________________|
     ''')
    break