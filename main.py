def f(x):
    return x**3 - 2*x**2 - 5

# Méthode de dichotomie
def dicho(a, b, tol, max_iter):
    results = []
    for k in range(max_iter):
        x_k = (a + b) / 2
        f_x_k = f(x_k)
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
results = dicho(a, b, tol, max_iter)

# Affichage des résultats
print("k   a^k             b^k              x^k               |f(x^k)|")
print("===========================================================================")
for k, a_k, b_k, x_k, f_x_k in results:
    print(f"{k:<2}   {a_k:<15.10f}    {b_k:<15.10f}     {x_k:<15.10f}      {f_x_k:<15.10f}")