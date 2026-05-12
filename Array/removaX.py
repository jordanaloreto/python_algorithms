#Dada uma lista e um número x, remova todas as ocorrências de x.
lista = [1, 2, 3, 2, 4, 2, 5]
x = lista.count(2)

for i in range(x):
    lista.remove(2)

print(lista)

