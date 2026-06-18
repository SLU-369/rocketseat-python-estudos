# Condicionais são : if, elif, else
# Exemplo de if: 
idade = 19 
print("exemplo de comando if :")
print('\n')
if idade >= 18:#MAIOR 
    print("Voce e maior de idade")
print('\n')
if idade == 19:#Voce tem EXTRITAMENTE essa idade 
    print('Voce tem 19 anos')
print('\n')
if idade <= 18:# MENOR
    print('Voce e menor de idade')
print('\n')
if idade != 10:# (!=) significa DIFERENTE
    print('Você é MENTIROSO! Não tem 10 anos')
print('\n')

# Else: 
if idade > 19:
    print('pode dirigir')
else:
    print('Não tirou a carteira ainda ? Ta duro ?')

#Elif
n_melancia = 3
if n_melancia < 1:
    print('não temos melancias')
elif n_melancia >= 1: #adiciona uma condição 
    print('temos melancias e da ate para dividir')
else:
    print('Vamos comer')
print('\n')
#tem um jeito de executar uma condição de if e else em uma unica linha.
mensagem = "pode tirar carteira de habilitação" if idade >= 18 else'Você não pode tirar a CNH'
