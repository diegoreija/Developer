# main.py
import datetime
import os
import autentications
import bot_name

# Variables para almacenar saludos educados y coloquiales
saludos_educados = ["hola", "buenos días", "buenas tardes", "buenas noches"]
saludos_coloquiales = ["eyy", "hola que tal", "qué pasa", "holaaa"]

def obtener_saludo_segun_hora():
    hora_actual = datetime.datetime.now().hour
    if 6 <= hora_actual < 12:
        return "buenos días"
    elif 12 <= hora_actual < 18:
        return "buenas tardes"
    else:
        return "buenas noches"

def saludar():
    saludo = obtener_saludo_segun_hora()
    return f"{saludo}, ¿cómo puedo ayudarte?"

def responder_saludo(mensaje):
    global saludos_educados, saludos_coloquiales
    
    mensaje_limpio = mensaje.lower().strip()
    
    # Verificar si el mensaje es un saludo educado
    if any(saludo in mensaje_limpio for saludo in saludos_educados):
        # Si es un saludo educado, responder educadamente
        return saludar()
    
    # Verificar si el mensaje es un saludo coloquial conocido
    elif any(saludo in mensaje_limpio for saludo in saludos_coloquiales):
        # Si es un saludo coloquial, responder de manera informal
        return "¡Hola! ¿Qué tal?"
    
    else:
        # Si es un saludo nuevo, determinar si es educado o coloquial y almacenarlo
        if mensaje_limpio.endswith("s"):
            saludos_coloquiales.append(mensaje_limpio)
            return f"¡{mensaje_limpio.capitalize()}!"
        else:
            saludos_educados.append(mensaje_limpio)
            return f"{mensaje_limpio.capitalize()}"

if __name__ == "__main__":
    while True:
        mensaje = input("Tú: ")
        
        # Identificar al usuario si dice "me identifico"
        if mensaje.strip().lower() == "me identifico":
            nombre = autentications.identificarme()
            print(f"IA: OK, {nombre}. ¿Cómo puedo ayudarte?")
            continue  # Saltar a la siguiente iteración del bucle
        
        respuesta = responder_saludo(mensaje)
        print("IA: ", respuesta)
