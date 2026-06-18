#Exercicio 1 (Cadastro Simples). Stacks: variaveis, input, print e formatação 
print("===== CADASTRO SIMPLES =====") 
print()
nome = input("Seja bem-vindo, qual o seu nome? ")
print()
idade = int(input(f"Maravilha {nome} e qual a sua idade?  ")) #Como você pode ver o (f) permitiu que eu colocasse a variavel nome para que eu personalizasse, por que se não daria erro o programa. 

if idade >= 18:
    print("Que isso em ta grandinho!!") 
    cidade = input("Mas me conta jovem você é de qual cidade ?")
else:
    print("Queria eu voltar a ser jovem assim, rsrs")
    cidade = input("Maravilha garoto, e você é de qual cidade ?")
