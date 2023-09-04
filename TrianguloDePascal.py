n = 5

# Patrón ascendente desde el centro
for i in range(n):
    for j in range(n - i): # Establecemos un ciclo nuevo en el cual imprimirá espacios en blanco hasta llegar a n-i, en este caso, 5
        print(" ", end="")
    for j in range(i * 2 + 1): # Realizamos un tercer ciclo en el cual imprimimos los * haste el valor calculado dentro de range()
        print("*", end="")
    print()

# Patrón descendente desde el centro
for i in range(n, -1, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i * 2 + 1):
        print("*", end="")
    print()