from defisurl import DefisUrl
# Connexion au défi et récupération des entrées
d = DefisUrl('https://codingup.univ-poitiers.fr/herewego/defis/ExempleURL/get/The_ZmaZe/7a524',
             verify=True)  # Mettez votre URL personnalisée ici
lignes = d.get()
# lignes = lignes[0].strip("--").strip(" ").split( )
# Affichage pour contrôle :
print("\n".join(lignes))

# À vous de travailler pour calculer la réponse :
res = int(lignes[0]) + int(lignes[1]) # On met ici 0, ce qui n'est probablement pas la bonne réponse...

# Affichage de la réponse pour contrôle et envoi :
print(res)
rep = d.post(res)
print(rep)