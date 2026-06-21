#while é o tipo de looping usado para repetir um bloco de codigo ENQUANTO uma condição for verdadeira. 
# Basicamente a estrutura dele é: ENQUANTO ISSO FOR VERDADEIRO, FAÇA ISSO. Quando essa condição se tornar falsa esse looping vai parar.
contador = 0 
while contador < 5:
    print("Contagem:", contador)
    contador += 1
# O que ta escrito aqui, o contador comeca com 0 no primeiro print, adiciona +1, a variavel contador agora vale 0+1 = 1, logo contador vale 1, repete o looping, printa 1 e soma mais um. A condção dela ser verdadeira [e ser menor do que 5, a medida que vai adicionando 1 uma hora ele vai chegar ate 5. Como ele tem que ser menor e não igual, ele para de executar pois virou falsa a condição. 
print("Programa finalizado!\n")

#BREAK: ele forç a pausa do looping 
vagas = 0

while True:
    print("Contagem:", vagas)
    vagas += 1 
    if vagas == 4:
        break
print("Programa Finalizado!")