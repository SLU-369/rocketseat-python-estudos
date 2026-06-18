# Criando um Dicionario de ex
pessoa = {"nome": "Samuel", "idade":30, "cidade": "Goiânia"}

# Acessando valores por chave 
print("nome:", pessoa["nome"])
print("idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

# Se eu quiser adicionar um valor ao dicionario ?
pessoa["sobrenome"] = "Uchoa" # assim adicionei mais um valor na chave dicionario 
print("sobrenome:", pessoa["sobrenome"])
print("\n")


#Podemos atualizar e remover um par de chave 
#REMOVENDO 
del pessoa["idade"]
print(pessoa) # se você perceber a idade 31 ja foi deletada

#Metodos Dicionario => keys(), values(), items()

chaves = list(pessoa.keys())#
print("Chaves do meu dicionario :", chaves)
print("\n")
#queo aceesar o indice 1 da nova lista Chaves:
print("O primeiro elemnteo das lista é: ", chaves[0])
# CHAVES ainda não virou uma lista temos que tranformar assim como (int) ou (float). usando o comando List
print("\n")
#Metodo Values
valores = list(pessoa.values())
print("Os valores do meu dicionario são: ", valores)
print("O primeiro elemnteo das lista é: ", valores[0])
print("\n")
#Metodos Items

itens = list(pessoa.items())
print("Pares chave-valor do dicionario :", itens) # Aqui virou uma tupla. 
#agora para mostrar o elemento da lista é diferente, veja:
print("Primeiro valor:", itens[0][1]) # o primeiro cochete (0) faz referencia ao primeiro chave valor que temos, Ja o segundo (1) = faz referencia a Samuel que é o elemento da chave valor nome. 

#para deixar mais claro 
print("Primeira chave-valor: %s = %s" %(itens[0][0], itens [0][1])) # primeiro %s é chave e o outro é o valor, o % seguido de parentese é para dar a função. Itens 00 mostra a chave nome e itens 01 mostra SAMUEL. Lembrando isso é pra  deixar organizado. 