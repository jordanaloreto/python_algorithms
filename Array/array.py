#Criar um array
frutas = []

#Adicionar elementos ao array
frutas = ['maca', ' uva', 'banana', 'laranja']

#printar o array
print("Array original: ", frutas)

#acrescentar um elemento ao array existente
frutas.append('pera')
print("Array append: ", frutas)

#remover um elemento do array
#Note: remove() s[o retira a primeira banana que aparecer, se tiver mais de uma banana no array ele tira a primeira que encontrar
frutas.remove("banana")
print("Array remove: ", frutas)

#indexar um array
terceiro_elemento = frutas[2]
print("Laranja indexado: ", terceiro_elemento)

#substituir um valor em array
fruta_nova = 'nectarina'
frutas[0] = fruta_nova
print("Substituicao da maca: ", frutas)