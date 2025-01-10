import os
def clearconsole():
    os.system('cls' if os.name == 'nt' else 'clear')
#APARTADO PARA LOS COPPYPASTES
#CARGANDO : cargando = input("Cargando... presiona enter para continuar")
#OPTIONS : option1 = ""
#option1 = ""
#option1 = ""
#option1 = ""
# PREGUNTAS : 1PREGUNTA= input("1 PREGUNTA! (presiona enter para continuar)")
#print("A.", option5)
#print("B.", option6)
#print("C.", option7)
#print("D.", option8)
#answer = input("Cual es tu respuesta?: ")
#if answer == "may" or answer == "min": 
  #score += 100
  #print("Correcto! me sorprendes...")
#else:
  #print("Nope, mal! muajajaj")


score = 0

option1 = "Cristobal colón"
option2 = "Julio C. Tello"
option3 = "Wolfgan Amadeus Mozart"
option4 = "Yo (Jonathan)"

option5 = "Huevo, aceite, ajos, sal y limón"
option6 = "Huevo, sal, limón y mostaza"
option7 = "De alacena"
option8 = "nose jejej"

option9 = "París"
option10 = "Estados unidos"
option11 = "Suiza"
option12 = "Pues en piza"

option13 = "Estrangulamiento"
option14 = "qué....?"
option15 = "Incinerarlo vivo"
option16 = "Contactar a un profesional"

option17 = ""
option18 = ""
option19 = ""
option20 = ""
  
print("bienvenido a QUIEN QUIERE SER MILLONARIO!")
username = input("A continuación, ingresa tu nombre:")

print(username)

print("este es tu nombre?")
answer1 = input("Y/N: ")
clearconsole()

if answer1 == "y" or answer1 == "Y":
  print("Bien, iniciemos!")
else:
  print("N O I M P O R T A... solo bromeo jeje")

cargando = input("Cargando... presiona enter para continuar")
clearconsole()

PRIMERAPREGUNTA= input("PRIMERA PREGUNTA! (presiona enter para continuar)")
print("Quién descubrió américa?")

print("A.", option1)
print("B.", option2)
print("C.", option3)
print("D.", option4)
  
answer = input("Cual es tu respuesta?: ")

if answer == "D" or answer == "d": 
  score += 100
  print("Correcto! (No sé cómo lo supiste la verdad...)")
else:
  print("Nope, era muy obvio...")

#PREGUNTA DOS TESTS (RECUERDA PONER EL CARGANDO SEGUIDO)
cargando = input("Cargando... presiona enter para continuar")
clearconsole()

SEGUNDAPREGUNTA= input("SEGUNDA PREGUNTA! (presiona enter para continuar)")
print("De qué está hecha la mayonesa?")

print("A.", option5)
print("B.", option6)
print("C.", option7)
print("D.", option8)
answer2 = input("Cual es tu respuesta?: ")
if answer2 == "A" or answer2 == "a": 
  score += 100
  print("Correcto! me sorprendes...")
elif answer2 == "C" or answer2 == "c":
  print("Cómo va a ser alacena???")
else:
  print("Nope, mal! muajajaj que tonto")
clearconsole()

#TERCERA

TERCERAPREGUNTA= input("TERCERA PREGUNTA! (presiona enter para continuar)")
print("Dónde queda la torre de piza")
print("A.", option9)
print("B.", option10)
print("C.", option11)
print("D.", option12)
answer3 = input("Cual es tu respuesta?: ")
if answer3 == "D" or answer3 == "d": 
  score += 100
  print("Correcto! eres muy inteligente...")
else:
  print("mal, cómo fallaste en esto?")

#CUARTA

CUARTAPREGUNTA= input("CUARTA PREGUNTA! (presiona enter para continuar)")
print("Cual es la forma más rápida de terminar con la existencia de otro individuo")
print("A.", option13)
print("B.", option14)
print("C.", option15)
print("D.", option16)
answer4 = input("Cual es tu respuesta?: ")
if answer4 == "D" or answer4 == "d": 
  score += 100
  print("bien, bastante bien...")
elif answer4 == "B" or answer4 == "b":
  print("Cómo que qué? te quedas sin puntos por no responder")
else:
  print("qué clase de respuesta es esta?")

#QUINTO

QUINTAPREGUNTA= input("QUINTA Y ULTIMA PREGUNTA! (presiona enter para continuar, bajo tu propio riesgo (T))")
print("Dónde")
print("Vives")
print("A.", option17)
print("B.", option18)
print("C.", option19)
print("D.", option20)
answer5 = input("Cual es tu respuesta?: ")
if answer5 == "T" or answer5 == "t": 
  score += 1100
  print("imposible, cómo supiste ese comando? no puedes haberme ganado nooooooooooo")
elif answer5 == "C" or answer5 == "c":
  score += 100
  print("Gracias.")
else:
  print("Bien...")  


if score == 0:
  print("Mal, todo mal, no vuelvas a jugar esto, nunca")
elif score == 100:
  print("100? Eso es todo? sólo una? voy a buscarte, desaparecerte y cometer asesinato contra ti")
elif score == 200:
  print("Dos de cinco, piensa un poco más, voy a buscarte y encontrarte")
elif score == 300:
  print("60%, te voy a buscar y no te va a gustar")
elif score == 400:
  print("400, nada mal para ser un humano")
elif score == 500:
  print("Puntaje perfecto, pero tu destino sigue siendo el mismo, la muerte")
elif score == 1000:
  print("Me derrotaste, pero no es suficiente, volveré")
elif score == 1100:
  print("eso es todo lo que tienes?")
elif score == 1200:
  print("Apesar de que obtuviste el código secreto, no respondiste bien, cuida tus espaldas")
elif score == 1300:
  print("No es un buen puntaje, cómo obtuviste el código...?")
elif score == 1400:
  print("No puedes haber descubierto el código, necesito escapar...")
elif score == 1500:
  print("Lo lograste!, no, no soy la consola, tranquilo, soy el creador! hiciste el puntaje perfecto y derrotaste a las maquinas")

print("Fin de el juego, gracias por jugar todos los derechos a gatoskint Bv")