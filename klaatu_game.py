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
print ("Pulsa cualquier tecla para abandonar el juego")

print()

option =  input("Escoge bien tu opción, este juego es un verdadero reto para cualquier humano, si eres valiente e inteligente adelante: ")
choice=option.lower()

if choice == "si":
    print()
    print("¡Brillante!, entonces doy por hecho que te gustan los grandes retos")
    
else:
    print("Bye Bye")
    sys.exit(0)
    input()

player=input("\n¿Cuál es tu nombre?: ")
print ("Hola,", player,"ahora también podrás conocerme. Observa bien la imagen y en ella encontrarás un nombre y clave secretos para poder seguir en el juego.\nRecuerda algo muy importante, debes hacer click en la imagen para cerrarla")
print()

from tkinter import *
from PIL import ImageTk
from PIL import Image

windows = Tk()
windows.title("Hola, soy Klaatu")
windows.destroy
imagen=ImageTk.PhotoImage(Image.open(r'C:\Users\perio\OneDrive\Escritorio\klaatu\klaatu_1.png').resize((500, 500)))

def close_windows():
    windows.destroy()

boton = Button(image=imagen, command=close_windows)
boton.pack()


#primer reto (Descubre el nombre de un espía secreto y la clave)
print ("Tienes tres intentos para descubrir tu usuario secreto y tu contraseña") #premisa del juego
print()

contador = 1
while contador <=3:
    jugador = input("Escribe el nombre del jugador secreto: ")
    usuario=jugador.lower()
    password = input("escribe la clave secreta: ")
    clave=password.lower()
    if usuario == "pax" and clave == "saturno":
        print()
        print ("¡Muy bien!", player, "ahora tienes acceso al juego")
        contador = 4
        print()
        print ("La clave que necesitas está encriptada y es la siguiente: . / + ¡ a < a")
        print()

       
        windows = Tk()
        windows.title("Desencripta tu clave con esta pista")
        windows.destroy
        imagen_2 = ImageTk.PhotoImage(Image.open(r'C:\Users\perio\OneDrive\Escritorio\klaatu\klaatu_2.png').resize((500, 500)))
        

        def close_windows2():
            windows.destroy()

        boton2=Button(image=imagen_2, command=close_windows)
        boton2.pack()



        contador = 1
        while contador <=3:
            challenge = input ("Escribe la respuesta: ")
            challenge1=challenge.lower()

            if challenge1 == "montaña":
                print()
                print ("Genial!!!")
                contador = 4
                print ()
                print ("Digamos que te planteo un reto matemático... ummm, veamos: ¿Cuál es el resultado de 12 + 30 + 33?")

                contador = 1
                while contador <=3:
                    acertijo_2 = int(input ("Escribe aquí tu respuesta:  "))
                    if acertijo_2 == 75:
                        print()
                        print ("¡Genial de nuevo!!!, seguimos a una nueva ronda")
                        print()
                        contador = 4
                        
                        contador = 1 
                        while contador <=3:
                            print ("Veo que vas muy bien en mates... que tal este pequeño desafío:")
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
                            if acertijo_3 == "d":
                                print()
                                print ("Correcto, pasas a una nueva ronda")
                                print ()
                                contador = 4 
                                                                                              
                            else:
                                print ("Perdiste")
                                contador = +1
                    else:   
                        print ("No, te equivocaste")
                        contador = contador +1
                  
            else:
                print ("No lo has logrado")
                contador = contador + 1
    else:
        print ("Haz fallado, vuelve a intentarlo")
        contador = contador + 1


print ("¿Quieres continuar en el Juego de Klaatu?")

print()
print("Escribe 'Sí' para jugar")
print()
print ("Pulsa cualquier tecla para abandonar el juego")

print()

option =  input(" ")
choice=option.lower()

if choice == "si":
    print()
    print("Ahora tus retos serán mayores, te deseo suerte!!!1")
    input()

else:
    print("Bye Bye")
    sys.exit(0)
    input()
