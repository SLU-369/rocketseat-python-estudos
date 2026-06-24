#Funções em Python é um bloco de codigos reutilizavel, consigo usa-lo varias vezes 
#Exemplo 

def comprimento(nome):
    print(f"\n Bom dia {nome}!")

print("\n Chamando o comprimento: ")
comprimento("Samuel")
comprimento("Falcon")

#Função  com retorno 
def quadrado(numero):
    resultado = numero ** 2
    return resultado
print("\n Chamando a Função quadrado: ")
resultado_quadrado = quadrado(5)
print("Rseultado:", resultado_quadrado)

#Função com multiplos parametros 
def soma(numero1, numero2):
    resultado= numero1 + numero2
    return resultado

print("\n Chamando a função soma: ")
numero1 = 20
numero2 = 50
resultado_soma = soma(numero1, numero2)
print("A soma do numero %s e o numero %s é: %s " % (numero1, numero2, resultado_soma))

#exercicios de fixação 

def calcular_o_dobro(numero):
    resultado = numero * 2
    return resultado

print("\nO resultado chamando a função é: ", )
numero = 33
resultado_dobro = calcular_o_dobro(numero)
print("O resultado é : ", resultado_dobro)

def verificar_maioridade(idade):
    if idade >= 18:
        return True
    else:
        return False
    
#desempacotamento
def contador(*num):
    tum = len(num)
    print(f"Recebi os valores {num} e são {tum} numeros! ")

contador(1, 2, 3, 4,  5)
contador(1, 3, 5)

#Listas eu vou criar uma lista e quero que cada valor dobre 
def dobra(lst):
    slu = 0
    while slu < len(lst):
        lst[slu]*=2
        slu+=1

lista = [1, 2, 3, 4, 5]

dobra(lista)
print()
print("A Lista dobrada é:", lista)

# for com desempacotamento 
def subtracao(*variavel):
    n = 0
    for sub in variavel:
        n-= sub
    print(f"subtraindo os valores {variavel}  temos {n}")

subtracao(1, 3)
subtracao(3, 4, 6)