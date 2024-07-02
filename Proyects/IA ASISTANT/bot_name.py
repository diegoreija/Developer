# name.py

import os

def obtener_nombre_bautizado():
    nombre_archivo = "bot_name.txt"
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r") as f:
            nombre = f.read().strip()
            return nombre
    else:
        return None

def bautizar_bot():
    nombre_archivo = "bot_name.txt"
    if os.path.exists(nombre_archivo):
        print("IA: El bot ya está bautizado.")
    else:
        nombre = input("Yo: Te voy a poner un nombre. ¿Cómo me voy a llamar a partir de ahora?: ").strip()
        with open(nombre_archivo, "w") as f:
            f.write(nombre)
        print(f"IA: El bot ha sido bautizado como '{nombre}'.")
