
# exercicio 6 do sexto capitulo

Cadastro, cadastro2 = {}

while True:
   nome = input("Digite o nome: ")
   if nome == "":
       break

   elif nome in Cadastro:
       print("O nome {} ja esta em cadastro". format(nome))
   idade = int(input('Idade: '))
   telefone = int(input('Telefone: '))

   Cadastro[nome] = (nome, idade, telefone)

print('Fim da primeira parte')

for nomes, dados in Cadastro.items():
    print(' Nome:    {}'.format(dados[0]))
    print(' idade    {}'.format(dados[1]))
    print(' Telefone {}'.format(dados[2]))

#
#





#Ordenar numeros

# for i in sorted(Cadastro, key = Cadastro.get):
#     print(i, Cadastro[i])





















