#Encontre o maior número da lista sem usar max().
lista = [3, 8, 1, 6, 2]
lista.sort(reverse=False)
print("Crescente: ", lista)
lista.pop(4)
print("Nova lista: ", lista)


