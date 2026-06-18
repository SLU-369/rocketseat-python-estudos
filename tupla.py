# Criando uma tupla de exemplo:
minha_tupla = (1, 2, 2, 3, 4)

print(minha_tupla[0]) # podemos fazer igual a lista 
print(minha_tupla[-1]) # podemos usar o indice negativo -1 para mostrar o ultimo elemento da tupla/lista

# minha_tupla[0] = 5 # não pode pois diferente da lista é imutavel. da erro 

# Metodo count: quantas vezes o termo se repete 
contagem = minha_tupla.count (2) # o 2 se repete 2 vezes 
print( "O termo 2 se repete: ", contagem, " Vezes")
 #Metodo  index

indice = minha_tupla.index(3)

# assim como em listas podemos procurar o indice pelo elemento. 