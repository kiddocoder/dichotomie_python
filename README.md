## Enoncé 

Soit la fonction polynomiale f(x) = x^3 - 2x^2 - 5 .
Avec python , ecrire un programme pour approximer la racine dans un interval
[1,3] par la methode de dichotomie avec une precision de 10^-7 .
Les donnees suivantes seront stockees dans un fichier sous forme de colonnes. le programme
doit s'arreter apres 23 iterations.
k   a^k             b^k              x^k               |f(x^k)|
=========================================================================
0   1.0000000000    3.0000000000     2.0000000000      1.0000000000
1   2.0000000000    3.0000000000     2.5000000000      2.5000000000
2   3.0000000000    2.5000000000     2.2500000000      2.2500000000
3   4.0000000000    2.2500000000     2.1250000000      2.1250000000
4   5.0000000000    2.1250000000     2.0625000000      2.0625000000
...     ...              ...             ...                ...

(a) Faire la representation graphique de f(x).
(b) Faire la representation graphique de l'evolution des x^k en focntion du nombre
des iterations k.
(c) Faire la representation graphique de l'evolution du residu en focntion du nombre
des iterations k.

Le programme devra stocker les figures dans des fichiers PDF sur le disque
dur dans un reperatoir appele 'Figures'.
