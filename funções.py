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