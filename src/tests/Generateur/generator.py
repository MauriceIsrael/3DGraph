import random
import math
import json
import couleurs 


colors = couleurs.getTableauCouleurs()
print(colors)

# Génération du jeu de données
jeu_de_donnees = {"Links": [], "Users":[] , "Lans":[], "Flows":[]}

rayon = 100

nbreNoeuds = 0
nbreLiens = 0

listeNC =[]
listeSat =[]
listeT =[]
listeLAN = []
listeU = []

interplan = 80
arcsup = 30

#Construction des noeuds R (coeurs et sat)
for i in range(12): 
    r = random.randint(rayon/2, rayon)
    alpha = random.randint(i*arcsup,(i+1)*arcsup)
    x = r*math.cos(alpha)
    y = 0*interplan
    z = r*math.sin(alpha)
    pointAncre1 = {"x": x, "y": y, "z":z}
    xx = x + random.randint(-10,10)
    yy= y
    zz = z + random.randint(-10,10)
    pointAncre2 = {"x":xx, "y":yy, "z":zz}
    listeNC.append(pointAncre1)
    listeNC.append(pointAncre2)


#Construction des noeuds sat avec double rattachement
paires = list(zip(listeNC[0::2], listeNC[1::2]))
for paire in paires:
    color = random.sample(colors, 1)[0]
    for _ in range(12):  #13
        pointAncre1 = paire[0]
        pointAncre2 = paire[1]
        rr = random.randint(0,rayon/4)
        aa = random.randint(0, 360)
        xx = rr*math.cos(aa) + (pointAncre1.get("x")+pointAncre2.get("x")/2)
        yy = 0*interplan
        zz = rr*math.sin(aa) + (pointAncre1.get("z")+pointAncre2.get("z")/2)
        pointSat = {"x": xx , "y": yy, "z":zz }
        listeSat.append(pointSat)
        jeu_de_donnees["Links"].append({"source": pointAncre1, "destination": pointSat, "color": color })    #plus simple de créer les liens à ce moment là
        jeu_de_donnees["Links"].append({"source": pointAncre2, "destination": pointSat, "color": color })    



#Construction des noeuds T
for point in listeNC:
    pointT = {"x":point.get("x"), "y":-1*interplan, "z": point.get("z")}
    listeT.append(pointT)
    jeu_de_donnees["Links"].append({"source": pointT, "destination": point, "color": color })    #plus simple de créer les liens verticaux T-R à ce moment là


 #Construction des points LAN

for point in random.sample(listeNC, 3):  #qques points issus des noeuds coeurs pour les 3 DC
    color = random.sample(colors, 1)[0]
    pointLAN = {"x":point.get("x"), "y":1*interplan, "z": point.get("z")}
    listeLAN.append(pointLAN)
    jeu_de_donnees["Links"].append({"source": pointLAN, "destination": point, "color": color })  
    jeu_de_donnees["Lans"].append({"type": "DC", "position": pointLAN, "color": color }) 

for point in random.sample(listeSat, int(len(listeSat)/4)):  #qques points issus des noeuds sat pour les usagers normaux
    color = random.sample(colors, 1)[0]
    pointLAN = {"x":point.get("x"), "y":1*interplan, "z": point.get("z")}
    listeLAN.append(pointLAN)
    jeu_de_donnees["Links"].append({"source": pointLAN, "destination": point, "color": color })  
    jeu_de_donnees["Lans"].append({"type": "user", "position": pointLAN, "color": color})   

#Construction des points Usagers
for point in random.sample(listeLAN, 10):
    pointU = {"x":point.get("x") + int(random.randint(-10,10)), "y":2*interplan, "z": point.get("z") + int(random.randint(-10,10))}
    listeU.append(pointU)
    jeu_de_donnees["Users"].append({"position": pointU})    

#Construction des liens

#Full Mesh entre les noeuds coeurs
color = random.sample(colors, 1)[0]
for source in listeNC:
    for dest in listeNC:
        if (source != dest):
            jeu_de_donnees["Links"].append({"source": source, "destination": dest, "color": color })    

#Construction des liens transport
paires = list(zip(listeT[0::2], listeT[1::2]))
for paire in paires:
    jeu_de_donnees["Links"].append({"source": paire[0], "destination": paire[1], "color": 'black' })  

#Construction des liens transport
paires = list(zip(listeT[1::3], listeT[2::4]))
for paire in paires:
    jeu_de_donnees["Links"].append({"source": paire[0], "destination": paire[1], "color": 'black' })  
    
# Flux usagers
for i in range(3):
    pointSource = random.sample(listeU, 1)[0]
    pointLAN1 = random.sample(listeLAN, 1)[0]
    pointSat1 = random.sample(listeSat, 1)[0]
    pointT1 = random.sample(listeT, 1)[0]
    pointT2 = random.sample(listeT, 1)[0]
    pointNC = random.sample(listeNC, 1)[0]
    pointT3 = random.sample(listeT, 1)[0]
    pointT4 = random.sample(listeT, 1)[0]
    pointSat2 = random.sample(listeSat,1)[0]
    pointLAN2 = random.sample(listeLAN, 1)[0]
    pointDest = random.sample(listeU, 1)[0]
    controlPoint =[pointSource,pointLAN1, pointSat1, pointT1, pointT2, pointNC, pointT3, pointT4, pointSat2, pointLAN2, pointDest]
    color = random.sample(colors, 1)[0]
    jeu_de_donnees["Flows"].append({"name":"Flow"+str(i), "controlPoint":controlPoint, "color": color })
    


# Enregistrement du jeu de données dans un fichier JSON
with open('../../../static/data.json', "w") as fichier:
    json.dump(jeu_de_donnees, fichier, indent=2)

print("Jeu de données enregistré avec succès.")
nbreNoeuds = len(listeLAN) + len(listeNC) + len(listeSat) + len(listeT) + len(listeU)
print("Nbre de noeuds: " + str(nbreNoeuds))
print("Nbre de liens: " + str(nbreLiens))



