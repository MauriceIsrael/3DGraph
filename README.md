# 3DGraph

Petit exemple de composants [Threlte](https://threlte.xyz/) utilisés pour représenter des plateaux, et un graphe en 2D dans chaque plateau
Un plateau pourrait représenter un WAN.
Le graphe serait la topologie du WAN formée par les noeuds et les liens entre les noeuds.

## Composants

* Le composant Plan représente un plan matérialisé par un disque.
* Le composant Link représente un lien entre une source et une destination:
    les sources/dest sont des petites sphéres. On trace un lien style "taper" entre les deux sphères. Si les liens sont verticaux, on les mets en pointillés.
* Le composant User est un petit cube avec une texture (en l'occurrence une image de user)
* Le composant Flow représente les flux usagers: une courbe de beziers passant par un certain nombre de points de controle.
* Le composant Lan est un petit disque sur le plan des réseaux usagers.
  
Une scene est crée avec le mode interactif pour pouvoir déplacer la caméra, une grille infinie et les composants précédents.

Le jeu de données est généré aléatoirement par un petit script Python.

pour le deploiement (ici sur Google Compute Engine)
* npm run build
* npm run prepare
* npm run deploy

enjoy!
