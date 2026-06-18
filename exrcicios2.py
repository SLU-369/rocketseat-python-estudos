
# Exercicio 2 - Cadastro de clientes Melhorado. 

print("==== Agendamento Barbearia ====")
print()
print()
nome = input("Qual seu nome e sobrenome? ")
#bom se eu soubesse faria com que apos "nome" ele verificasse se o cliente é nomo no banco de dados ou não. Se novo ele se apresentaria, se ja é de casa ele falaria " bom te ver de novo meu amigo " 
print("prazer", nome, "me chamo Jarvis e sou a IA da Barbearia  Mr. Magno" )
data_hora = input(f"Para qual dia e qual horário, {nome}, você gostaria de agendar? ")
#Apos isso com o conhecimento necessario ele verifica a agenda e fala se horario escolido esta ou não disponivel respeitando um intervalo de tempo de 30 min de cada agaendamento, pois é o tempo medio que dura um corte. 
print()
print(nome, "olha temos vaga sim na agenda, podemos confirmar esse agendamento ? ", "AGENDAMENTO DATA/HORA: ", data_hora)

y_n = input("digite (y) para confirmar e (n) para não. ")
print()
print()
if y_n == "y":
    print("Maravilha seu agendamento foi confirmado para o dia e hora: ", data_hora)
else:
    print("Ok, Gostaria de alguma informação ou de agendar para algum outro dia?")
#Aqui seria bom se eu conhecesse de Loop pois ficaria em um loop verificando se a resposta vai ser y ou n, e criar uma pergunta de se ele gostaria de finalizar o atendimento 
