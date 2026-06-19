""" for, é o momento que você deixa de pensar: 
“Vou fazer isso para uma coisa.”
E começa a pensar:
“Vou fazer isso para várias coisas automaticamente.” """

#LOOPs = for
#Analogia para entender (for): Imagine uma fila 
clientes = ["Carlos", "Rafael", "Bruno"]
for cliente in clientes:
    print("Chamando", cliente)
""""Como resultado: 
Chamando Carlos
Chamando Rafael
Chamando Bruno"""

#O for é como a recepcionista passando pela lista de nomes e chamando um por um.

#Tuplas
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print("\n", elemento)

#Dicionario 
pessoa = {"nome": "Samuel", "Idade": 23, "Cidade": "Goiânia"}
print("\n For utilizando dicionario - Chaves")
for chaves in pessoa.keys():
    print("\n", chaves)

print("\n For utilizando dicionario - Valores")
for valores in pessoa.values():
    print("\n", valores)

print("\n For utilizando dicionario - Chaves e valores")
for chaves, valores in pessoa.items():
    print("\n")
    print(f"{chaves}: {valores}")

# range (): Retorna um intervalo de numero em formato de lista. Ex:

numeros = list(range(10))
print("\n", numeros)

#len (): pregunt: Quantos elementos existem aqui?

print("\n Utilizando a função renge() com len()")
lista = list(range(6))
print("\n", lista)
for indice in range(0, len(lista)):#6 elementos mas como o range diminui 1 vai ficar 4 o indice  
    print("indice:", indice)
    print('elemento: ', lista[indice])
if indice == 3:
    lista[indice] = 5
else:
    lista[indice] = 0
print(lista)

#Enumerate () : me retorna o indice e o valor junto sem eu precisar Lista[indice]. 

lista_enumerate = ["a", "B", "C"]
for indice, valor in enumerate(lista_enumerate):
    print("\n", f"{indice}: {valor}")
    if indice == 1:
        print("indice 1")
