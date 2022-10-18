"""

Posicionamiento de jugadores 
Crear cuenta 
Ingresa nombre de jugador
Ingresa contraseña
"Hora de iniciar sesión"
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
'NICKK107': 82050,}

import operator
clients_sort = sorted(lista.items(), key=operator.itemgetter(1), reverse=True)
for name in enumerate(clients_sort):
    print(name[1][0], ':', lista[name[1][0]])
