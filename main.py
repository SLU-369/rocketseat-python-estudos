inicio = int(input("Número de início da contagem: "))
fim = int(input("Número de fim da contagem: "))

if inicio < fim:
    # contagem progressiva
    while inicio <= fim:
        print(inicio)
        inicio += 1

elif inicio > fim:
    # contagem regressiva
    while inicio >= fim:
        print(inicio)
        inicio -= 1

else:
    print(inicio)