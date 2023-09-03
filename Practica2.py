# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 11:33:00 2023

@author: guill
"""

base_de_datos = {
    "Hola": "¡Hola! ¿Cómo estás?\n",
    "Como estas?": "Estoy aquí para ayudarte. ¿De qué te gustaría hablar?\n",
    "de que te gustaria hablar?": "Estoy aquí para responder tus preguntas. ¿En qué tema estás interesado?\n"
}

print("Sistema: Hola, ¿en qué puedo ayudarte?")

while True:
    usuario_input = input("Usuario: ")
    
    if usuario_input.lower() == "salir":
        print("Sistema: Hasta luego. ¡Vuelve pronto!")
        break
    
    if usuario_input in base_de_datos:
        print("Sistema:", base_de_datos[usuario_input])
    else:
        nueva_pregunta = input("No tengo información sobre eso. ¿Puedes proporcionar más detalles para agregar conocimiento nuevo? ")
        base_de_datos[usuario_input] = nueva_pregunta
        print("Nuevo conocimiento agregado a la base de datos.")
        print("Sistema: Gracias por la información. Lo tendré en cuenta.")
