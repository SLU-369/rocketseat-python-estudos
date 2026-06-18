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