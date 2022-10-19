

#Proyecto

#Posicionamiento de jugadores competitivos (shooters)

#A lo largo delos años los gamers han comtetido por ser los mejores del mundo y para eso se han organizado varios torneos de diferentes juegos. Sin embargo la mayoria de las veces solo se sabe quien es el mejor jugdor cuando el torneo ha concluido, pero antes del torneo nadie sabe quien es mejor, por lo que planeo diseñar un programa que clasifique a los jugadores para saber quien es el mejor de todos en ese momento.

#El programa tomara los datos de eliminaciones y victorias del jugador para luego sumarlos y asi tener un resultado que mostrara una cierta cantidad de puntos (un numero) y el programa los clasificara de mayor a menor.

#Inicio

#dar la bienvenida

#crear cuenta

#iniciar sesión

#ingresar el numero de eliminaciones y vicotrias

#imprimir lista

#score= eliminaciones+victorias

#si score> 8000

#agregar jugador en la lista

#sino puntos insuficientes

#te faltan "puntos" para clasificarte

#fin

#Los avances estan en la carpeta de avances.py, las otras carpetas contienen los avances anteriores pero contienen errores. Avance 2

#En este avance se incorporaron sumas y restas para saber cuantos puntos tiene el jugador y para saber si le faltaban puntos para clasificarse

#Avance 3

#En este avance se incorporaron funciones para dar la bienvenida y para dar las conclusiones para cuando el jugador sepa si esta dentro del ranking o no

#Avance 4

#Se añadieron condicionales para cuando se cumplieran los puntos minimos y tambien para saber si el programa tiene que restar la cantidad de puntos por 8000#

#Avance 5

#Se añadieron ciclos while para que el usuario ingrese una cuenta y contraseña y en caso de que estos sean incorrectos se correra el ciclo haste que la condición sea correcta.

#Avance 6

#Se añadieron listas para que guarden los puntos de los jugadores

#Avance 7

#Se añadió un diccionario para que guradara los puntos de los jugadores y esta se imprime de mayor a menor en relación a los puntos.


def bienvenida():
    print ("Bienvenido al sistema de ranking de videojuegos")

def conclusiones ():
    if score>8000 :
        print("feliciades ", jugador, " has logrado casificarte en el ranking con ", score, " puntos")
    else :
        print ("lo sentimos ", jugador, "tienes ", score, " puntos y no son suficientes para entrar en el ranking")
        print("lo minimo para clasificarte es de 8000 puntos")
        print("Te faltan ", res, " puntos para entrar al ranking")

bienvenida()
                                                              #Creación de cuenta
print ("cree una cuenta")
jugador= input ("ingrese su nombre de jugador")
contrasena= input ("ingrese una contraseña")

print("Tu cuenta a sido creada")
print ("llego la hora de iniciar sesión")
                                                     #Inicio de sesión
IGN= input ("escriba su IGN")

while IGN!= jugador :
    print ("nombre de jugador incorrecto")
    IGN= input ("ingrese su IGN")

print ("¡Bienvenido ", jugador ," !")
password= input("ingrse la contraseña")

while password != contrasena:
    print ("contraseña incorrecta")
    print ("¿seguro que eres ", jugador, " ?")
    password= input ("ingrese la contraseña")

print ("¡Bienvenido!", jugador)
print("Necesitamos algunos datos para saber si entras en el ranking")
                                                                            #Calculo de puntos
kills= float(input("ingresa el numero de kills"))
wins= float(input("ingresa tus victorias magistrales"))
score= kills+wins

                     
                                     #lista de jugadores
lista = {'romax': 34553,
'Rotrex': 42484,
'Marmota_Espacial': 24285,
'CtC c3jo': 89700,
'ViccenialWharf9': 589208,
'Pablito on 60hz': 540278,
'CrazyHand4': 506890,
'G2EcatepecTelmex': 10852,
'Octavio_Luna333': 25084,
'rockielchido666':54085,
'AverageEar554789':54508,
'HitherMcfly':45050,
'Jespartan117':54088,
'XxFred45xX': 59809,
'Bugha': 520860,
'Carlosgamer': 20898,
'Raptor yt': 52580,
'NRG Clix': 51808,
'FaZe Martoz': 481080,
'Mongraal': 78096,
'NRG Pablo Escobar': 52109,
'Dripzz': 249509,
'Mistik_Codee': 65078,
'AlanCQ': 750874,
'CrizzXR52': 5870605,
'JorgeIsaac115': 41801,
'FaZe Cerdillo': 565078,
'MinLeyva': 10780,
'HunterSalomon': 10080,
'Forastero YT': 51080,
'BossKyu':50290,
'DigitalReaper08':10545,
'Ricardo Navaja': 9485,
'Faze ShodOcean': 70587,
'AghastGalaxy477': 408745,
'AllergicToast95': 45054,
'BragBird8336805': 54054,
'CaptainOliva': 8505,
'CRSllorchX': 51500,
'BlazingWinter': 50450,
'VGR Cizzorz': 48408,
'Dair Extreme96': 41057,
'Daninja243': 42080,
'DDP117': 50200,
'Delogram': 40850,
'DigitalReaper08': 41080,
'DrabSky80692391': 10400,
'Duckling378': 100274,
'FixableRook3877': 508450,
'Genial X': 41028,
'HerbalLemur5136': 24508,
'Jommae': 65087,
'juandavo04': 50800,
'Komplex08Xx': 50700,
'LiliBA28': 45085,
'MaxScreamer21': 8017,
'mugr0son': 540181,
'Nach72': 50710,
'nutria': 74058,
'PriorPenguin': 10800,
'RainbowGull6471': 54070,
'SaffronMocha814': 42078,
'StatelyPlanet96': 74057,
'StronCookie307': 54058,
'Tac0sDeJamAicA': 41178,
'Tailon Dragon': 21004,
'TFG P4nthom': 48780,
'VALMAX': 50500,
'VGR Alexis': 50870,
'VGR Monster': 417040,
'VGR Taco': 65805,
'VGRflame88': 87205,
'WeeklongEel1': 50878,
'Wtz manu': 50710,
'YMAH DassCat': 108820,
'zKyre': 40578,
'ZtMowgli60': 55100,
'Zeathos': 810048,
'Rash vBi': 50642,
'Gooner022': 8408,
'Azgan': 28780,
'dark drag601': 50604,
'Titantium': 50518,
'FuzzWavve': 40570,
'SIRKOBE24': 52306,
'fl8365': 80500,
'XwlluisX': 40870,
'xXNoble6Xx96': 540570,
'DANI1298': 80550,
'LegoKyle': 457087,
'OskaarPeem': 50507,
'CidoTheCreatlor': 28507,
'Ratedshotgun19': 5840780,
'jose117esnaiper': 8705,
'Dr Marvel': 78050,
'Dr. Nopal': 40878,
'CRSlWilow': 75000,
'JxRiTTeRx360': 75080,
'paco zubaran': 40200,
'NICKK107': 82050,
jugador: score}
                             #si el puntaje no cumple con el minimo entonces se cacularan los puntos faltantes
if score < 8000:
    del lista[jugador]
    lista
    res= 8000-score
                                                                                  #imprime la lista de mayor a menor en relación a los puntos
import operator
clients_sort = sorted(lista.items(), key=operator.itemgetter(1), reverse=True)
for name in enumerate(clients_sort):
    print(name[1][0], ':', lista[name[1][0]])

conclusiones ()
