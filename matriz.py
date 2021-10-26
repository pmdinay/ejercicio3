"""Suma de dos matrices"""
n = int(input("Dimension de matrices a sumar: "))
matrix1 = []
print("Elementos de la matriz 1: ")
for i in range(n):
    fila = []
    for j in range(n):
        print("Elemento", i, "," ,j)
        elem = float(input("Elemento: "))
        fila.append(elem)
        matrix1.append(fila)
print("Matriz 1 leída: ", matrix1)

matrix2 = []
print("Elementos de la matriz 2: ")
for i in range(n):
    fila = []
    for j in range(n):
        print("Elemento", i, "," ,j)
        elem = float(input("Elemento: "))
        fila.append(elem)
        matrix2.append(fila)
print("Matriz 2 leída: ", matrix2)

m_suma = []
for  i in range(n):
    elem = matrix1[i][j] + matrix2[i][j]
    fila.append(elem)
    m_suma.append(fila)
    print("Matriz suma: \n", m_suma)


