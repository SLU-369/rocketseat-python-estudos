#Declaração de uma lista 
minha_lista = [1, 2, 3, 4, 5, "Samuel", True, False]
#Exibir a Lista 
print("Essa é a lista que eu criei: ", minha_lista)

#Consigo Fazer mudaças dos elementos da lista, atribuindo um outro valor
 
minha_lista [0] = "Python" #Agora não vale mais 1, Vale Python 

#Exibindo apenas o termo que eu quiser na lista. Usa-se os cochetes que aprendemos e escrevemos o indice. que inicia de 0 a 7 nesse caso 

print("O primeiro numero de indice 0 é: ", minha_lista[0])

# Fatiando, ou seja escolhendo intervalo 

print('minha lista do numero 2 ao true: ', minha_lista[1:7])

#Metodos de Listas 

# Metodo Append (): Adiciona um elemento ao  final da lista 

minha_lista.append(6)
print("Apos utilizar o comando append, minha lista ficou assism: ", minha_lista)

#Metodo Index: Serve para retornar o indice do elemento que eu quero.
idade = minha_lista.index(6)
print("O indice do elemento 6 é: ", idade)

#Metodo Insert: Insere um elemento em um indice especifico.
minha_lista.insert(2, 10)
print("Esse sera o elemento que ira ficar no lugar do numero 3:", minha_lista)

# Metodo pop: remove e retorna um elemento de um indice especifico. No POP é igual ao metodo de fatiar se quero remover o indice 3 tenho que escrever o 4, ou seja um a mais. 
elemento_removido = minha_lista.pop(4)
print("O elemento Removido foi: ", elemento_removido)
print("apos POP(4) : ", minha_lista)

#Metodo Remove: Diferente do pop que remove por indice, ele remove pelo valor 

minha_lista.remove(True)
print("Minha lisata apos remove(True)", minha_lista)

# Metodo Sort: Organiza a lista de forma crescente 

minha_lista.sort() #so funciona com numeros se tiver STR e booleano ele não reconhece.
