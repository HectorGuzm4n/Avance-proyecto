"""

Posicionamiento de jugadores competitivos
Inicio
puntaje= []
puntaje.sort ()
Ingresar nombre de jugafor y contraseña
mientras constraseña != contraseña
entonces
Imprimir ("su contraseña es incorrecta")
definir "score" como entero
Leer kills
leer wins
score= kills+wins
Imprimir score
si score < 8000 entonces
imprimir ("tus puntos no son suficientes para rankearte")
SiNO
imprimir ("felicidades has logrado clasificarte en el ranking con ", score)
puntaje.insert (5,score)
puntaje.sort ()
print (puntaje [1])
print (puntaje [2])
print (puntaje [3])
print (puntaje [4])
print (puntaje [5])
fin
"""


print ("cree una cuenta")
jugador= input ("ingrese su nombre de jugador")
contrasena= input ("ingrese una contraseña")

print ("llego la hora de iniciar sesión")

IGN= input ("escriba su IGN")

while IGN!= jugador :
    print ("jugador no encontrado")
    IGN= input ("ingrese su IGN")

print ("¡Bienvenido ", jugador ," !")
password= input("ingrse la contraseña")

while password != contrasena:
    print ("contraseña incorrecta")
    print ("¿seguro que eres ", jugador, " ?")
    password= input ("ingrese la contraseña")

print ("¡Bienvenido!")

kills= float(input("ingresa el numero de kills"))
wins= float(input("ingresa tus victorias magistrales"))

score= kills+wins

if score>8000 :
    print("feliciades ", jugador, " has logrado casificarte en el ranking con ", score, " puntos")
else :
    print ("lo sentimos ", jugador, "tienes ", score, " puntos y no son suficientes para entrar en el ranking")
  
  stats= {wins, kills}
  
ranking= [[nombre , score], [stats] ]          //los valores de la lista variaran dependiendo del juego y los puntos de cada jugador con una cuenta vinculada//
ranking.sort ()
ranking.insert (5,score)
ranking.sort ()
  
  print ("nombre   puntuación   Victorias   Eliminaciones")
  print (ranking [1])
  print (ranking [2])
  print (ranking [3])
  print (ranking [4])
  print (ranking [5])
  print (ranking [6])
  print (ranking [7])
  print (ranking [8])
  print (ranking [9])
  print (ranking [10])
  print (ranking [11])
  print (ranking [12])
  print (ranking [13])
  print (ranking [14])
  print (ranking [15])
  print (ranking [16])
  print (ranking [17])
  print (ranking [18])
  print (ranking [19])
  print (ranking [20])
  print (ranking [21])
  print (ranking [22])
  print (ranking [23])
  print (ranking [24])
  print (ranking [25])
  print (ranking [26])
  print (ranking [27])
  print (ranking [28])
  print (ranking [29])
  print (ranking [30])
  print (ranking [31])
  print (ranking [32])
  print (ranking [33])
  print (ranking [34])
  print (ranking [35])
  print (ranking [36])
  print (ranking [37])
  print (ranking [38])
  print (ranking [39])
  print (ranking [40])
  print (ranking [41])
  print (ranking [42])
  print (ranking [43])
  print (ranking [44])
  print (ranking [45])
  print (ranking [46])
  print (ranking [47])
  print (ranking [48])
  print (ranking [49])
  print (ranking [50])
  print (ranking [51])
  print (ranking [52])
  print (ranking [53])
  print (ranking [54])
  print (ranking [55])
  print (ranking [56])
  print (ranking [57])
  print (ranking [58])
  print (ranking [59])
  print (ranking [60])
  print (ranking [61])
  print (ranking [62])
  print (ranking [63])
  print (ranking [64])
  print (ranking [65])
  print (ranking [66])
  print (ranking [67])
  print (ranking [68])
  print (ranking [69])
  print (ranking [70])
  print (ranking [71])
  print (ranking [72])
  print (ranking [73])
  print (ranking [74])
  print (ranking [75])
  print (ranking [76])
  print (ranking [77])
  print (ranking [78])
  print (ranking [79])
  print (ranking [80])
  print (ranking [81])
  print (ranking [82])
  print (ranking [83])
  print (ranking [84])
  print (ranking [85])
  print (ranking [86])
  print (ranking [87])
  print (ranking [88])
  print (ranking [89])
  print (ranking [90])
  print (ranking [91])
  print (ranking [92])
  print (ranking [93])
  print (ranking [94])
  print (ranking [95])
  print (ranking [96])
  print (ranking [97])
  print (ranking [98])
  print (ranking [99])
  print (ranking [100])

