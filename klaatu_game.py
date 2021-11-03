#maqueta de programa "El juego de Klaatu"
import sys
import tkinter as tk
import pyfiglet

word=pyfiglet.figlet_format ("El juego de Klaatu")
print (word)

print ("Soy Klaatu, un extraterrestre amistoso.\nVengo de otra galaxia a retar a los humanos con un juego de inteligencia.\nQuiero jugar contigo")

print()
print("Escribe 'Sí' para jugar")
print()
print ("O pulsa cualquier tecla para abandonar el juego")

print()

option =  input("Escoge bien tu opción, este juego es un verdadero reto para cualquier humano, si eres valiente e inteligente adelante: ")
choice=option.lower()

if choice == "si":
    print()
    print("********************************************************************")
    print("¡Brillante!, entonces doy por hecho que te gustan los grandes retos")
    print("********************************************************************")

else:
    print("Bye Bye")
    sys.exit(0)
    input()

player=input("\n¿Cuál es tu nombre?: ")
avatar=pyfiglet.figlet_format (player)
print (avatar)
print ("Hola,", player,"ahora también podrás conocerme.", "\nObserva bien la imagen y en ella encontrarás un nombre y clave secretos para poder seguir en el juego.")
print ("Recuerda algo muy importante, debes hacer click en la imagen para cerrarla cuando lo descubras")
print ()

from tkinter import *
from PIL import ImageTk
from PIL import Image

windows = Tk()
windows.title("Hola, soy Klaatu")
imagen=ImageTk.PhotoImage(Image.open(r'C:\Users\perio\OneDrive\Escritorio\klaatu\klaatu_1.png').resize((500, 500)))
windows.destroy


def close_windows():
    windows.destroy()

boton = Button(image=imagen, command=close_windows)
boton.pack(ipadx=15, ipady=10)



#primer reto (Descubre el nombre de un espía secreto y la clave)
print ("**********************************************************************")
print ("Tienes tres intentos para descubrir tu usuario secreto y tu contraseña") #premisa del juego
print ("**********************************************************************")

contador = 1
while contador <=4:
    jugador = input("Escribe el nombre del jugador secreto: ")
    usuario=jugador.lower()
    password = input("escribe la clave secreta: ")
    clave=password.lower()
    if usuario == "pax" and clave == "saturno":
        print()
        print ("¡Muy bien!", player, "ahora tienes acceso al juego")
        break
    else:
        print ("Haz fallado, vuelve a intentarlo")
        contador = contador +1
    if contador == 4:
        sys.exit(0)
        input()


print(
"""
+==================================+
| Hay una clave que necesitas      |
| y está encriptada así:           | 
|    5 " ¡ $ a ¡ 5 $ $ 5 ) ¡ $ 5   |
+==================================+
""")

       
windows = Tk()
windows.title("Desencripta tu clave con esta pista")
imagen_2 = ImageTk.PhotoImage(Image.open(r'C:\Users\perio\OneDrive\Escritorio\klaatu\klaatu_2.png').resize((500, 500)))
windows.destroy

        
def close_windows2():
    windows.destroy()
    
boton2=Button(image=imagen_2, command=close_windows)
boton2.pack()

contador = 1
while contador <=4:
    challenge = input ("Escribe la respuesta: ")
    challenge1=challenge.lower()

    if challenge1 == "extraterrestre":
        print()
        print ("Genial!!!")
        break
    else:
        print("No es correcto")
        contador = contador + 1
    if contador ==4:
        sys.exit(0)
        input()


print(
"""
+==================================+
| Digamos que te planteo este      |
| reto matemático....              |
| ¿Cuál es el resultado de la suma:|
|        12 + 30 + 33 ...?         |
+==================================+
""")

contador = 1
while contador <=4:
    acertijo_2 = int(input ("Escribe aquí tu respuesta:  "))
    if acertijo_2 == 75:
        print()
        print ("¡Genial de nuevo!!!, seguimos a una nueva ronda")
        print()
        break
        
    else:
        print ("Fallaste")
        contador = contador + 1
    if contador ==4:
        sys.exit(0)
        input()


print(
"""
+==================================+
| Ummm, te crees especial.....     |
| Veo que vas bien en mates        |
| ¿Qué tal este desafío?           |
+==================================+
""")

contador = 1 
while contador <=4:
        print()
        print ("Debes elegir cuál de las siguientes relaciones es incorrecta")
        print()
        print ("a. 55 < 56")
        print ("b. 112 > 99")
        print ("c. 481 < 484")
        print ("d. 57 > 67")
        print ("e. 35 > 33")
        print()
        acertijo_3 = input ("Introduce aquí la letra de la respuesta:  ")
        if acertijo_3 != "d":
            print()
            print ("... incorrecto")
            print ()
            contador = contador +1 
            if contador == 4:
                sys.exit(0)
                input()

        else:
            acertijo_3 == "d"
            print ("Eres un ganador")
            break
            #sys.exit (0)
            #input()


print(
"""
+==================================+
| Bienvenido a otro desafío.       |
| Introduce un número impar entre  |
| entre 0 y 10 y adivina cuál      |
| es el número secreto             |
| Tienes solo 3 oportunidades, y   |  
| 5 opciones diferentes....        | 
| ¿te atreves?                     |
+==================================+
""")
numeroSecreto = 7 

contador = 1
while contador <= 4:
    choice=int(input("Ingresa tu número: "))
    if choice == numeroSecreto:
        print()
        print ("Acertaste, realmente sois brillante")
        break
    #print("tu elección", choice) 

    else:
        print ("Has fallado")
        contador = contador + 1
        if contador == 4:
            sys.exit(0)
            input()



print(
"""
+==================================+
|    Un grupo de niños muy listos  |
|    debía calcular cuántos de     |
|    ellos podrían jugar en tres   | 
|    servidores diferentes de      | 
|    Roblox. Cada uno de los       |
|    servidores acepta a 4         |
|    jugadores. Y al final dan     |
|    una recompensa para que se    |
|    unan  5 jugadores más...      |
|                                  |  
|                                  | 
|                                  |
| Calcula la siguiente operación:  | 
|   4 x 3 + 5 = ?                  | 
+==================================+
""")
total = 17 

contador = 1
while contador <= 4:
    choice=int(input("Ingresa tu número: "))
    if choice == total:
        print()
        print ("Has vuelto a ganar")
        break
    
    else:
        print ("Has fallado")
        contador = contador + 1
        if contador == 4:
            sys.exit(0)
            input()

input ()

