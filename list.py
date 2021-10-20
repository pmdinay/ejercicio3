""" Ejemplo bucles """
data = list()
while True:
    entrada = float(input("Siguiente dato (10 para terminar)?: "))
    if entrada != 10.0 :
        data.append(entrada)
    else:
        break

for dato in data:
    print("Número: ", dato)