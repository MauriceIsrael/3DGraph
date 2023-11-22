# 3DGraph

Petit exemple de composants [Threlte](https://threlte.xyz/) utilisés pour représenter des plateaux, et un graphe en 2D dans chaque plateau
Un plateau pourrait représenter un WAN.
Le graphe serait la topologie du WAN formée par les noeuds et les liens entre les noeuds.

##Composants

le composant Plan représente un plan matérialisé par un disque
Le composant Link représente un lien entre une source et une destination:
    les sources/dest sont des petites sphéres
    on trace un lien style "taper" entre les deux sphères.
    Si les liens sont verticaux, on les mets en pointillés

Le jeu de données est généré aléatoirement par un petit script Python.
