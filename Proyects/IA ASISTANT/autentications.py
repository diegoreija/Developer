# autentication.py

import os
import re

def identificarme():
    while True:
        mensaje = input("Tú: ").strip().lower()
        
        if mensaje == "me identifico":
            nombre = input("IA: ¿Quién eres?: ").strip()
            return nombre
        else:
            print("IA: No entiendo. ¿Cómo puedo ayudarte?")

def verificar_owner(nombre):
    nombre_correcto = obtener_nombre_owner()
    return nombre == nombre_correcto

def obtener_nombre_owner():
    nombre_archivo = "owner_data.txt"
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r") as f:
            data = f.read()
            match = re.search(r'NombreDePila:\s*(\w+)', data)
            if match:
                return match.group(1)
            else:
                return None
    else:
        return None
