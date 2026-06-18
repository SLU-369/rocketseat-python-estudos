#Declaração 
nome_completo = "Samuel Uchoa"
nome_completo_aspas ="""Samuel 
Uchoa"""
nome_completo_barra = "Samuel \
    Uchoa"
nome = "Samuel"
sobrenome = "Uchoa"
#Formatação 
print("nome completo (1a Forma):", nome_completo) 
print("nome completo (2a Forma):" + nome_completo)
print("nome completo (3a Forma):" + "Samuel" + "Uchoa")
print("nome completo (4a Forma):" + nome, sobrenome)
print("nome completo (7a Forma):%s" % nome_completo)
print("nome completo (8a Forma):%s %s" % (nome, sobrenome))
print(f"nome completo (9a Forma): {nome} {sobrenome}")
print("nome completo (10a Forma): {} {}".format(nome, sobrenome))
print(nome.count("a")) #Conta quantas letras A tem dentro da Variavel nome
print(nome[0])