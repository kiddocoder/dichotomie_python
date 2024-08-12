import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Définition de la fonction
def f(x):
    return x**3 - 2*x - 5

# Méthode de dichotomie
def dichotomie(a, b, tol, max_iter):
    results = []
    for k in range(max_iter):
        x_k = (a + b) / 2
        f_x_k = f(x_k)  # Appel de la fonction f
        results.append((k, a, b, x_k, abs(f_x_k)))
        if abs(f_x_k) < tol:
            break
        if f(a) * f_x_k < 0:
            b = x_k
        else:
            a = x_k
    return results

# Paramètres
a = 1
b = 3
tol = 1e-7
max_iter = 23

# Exécution de la méthode de dichotomie
results = dichotomie(a, b, tol, max_iter)

# Sauvegarde des résultats dans un fichier avec formatage
output_file = 'results.txt'
with open(output_file, 'w') as file:
    # Écriture des en-têtes
    file.write("k    a^k                b^k                x^k                  |f(x^k)|\n")
    file.write("============================================================================\n")

    # Écriture des résultats
    for k, a_k, b_k, x_k, f_x_k in results:
        file.write(f"{k:<2}   {a_k:<15.10f}    {b_k:<15.10f}     {x_k:<15.10f}      {f_x_k:<15.10f}\n")

# Création du répertoire pour les figures
if not os.path.exists('Figures'):
    os.makedirs('Figures')

# (a) Représentation graphique de f(x)
x = np.linspace(0, 4, 400)
y = f(x)
plt.figure()
plt.plot(x, y, label='f(x) = x^3 - 2x - 5')
plt.axhline(0, color='gray', lw=0.5, ls='--')
plt.axvline(0, color='gray', lw=0.5, ls='--')
plt.title('Représentation de f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.savefig('Figures/f_x.pdf')
plt.close()

# (b) Représentation graphique de l'évolution des x^k
plt.figure()
plt.plot([k for k, *_ in results], [x_k for *_, x_k, _ in results], marker='o')
plt.title("Évolution de x^k en fonction des itérations k")
plt.xlabel('k')
plt.ylabel('x^k')
plt.grid()
plt.savefig('Figures/evolution_xk.pdf')
plt.close()

# (c) Représentation graphique de l'évolution du résidu
plt.figure()
plt.plot([k for k, *_ in results], [f_x_k for *_, _, f_x_k in results], marker='o', color='red')
plt.title("Évolution du résidu en fonction des itérations k")
plt.xlabel('k')
plt.ylabel('|f(x^k)|')
plt.yscale('log')  # Utilisation d'une échelle logarithmique pour mieux voir l'évolution
plt.grid()
plt.savefig('Figures/evolution_residu.pdf')
plt.close()

print(f"Les résultats ont été sauvegardés dans '{output_file}' et les figures dans le répertoire 'Figures'.")