Alunos = {}

while True:
    matr = int(input("  Digite a matrícula: "))
    if matr == 0:
        break
    elif matr in Alunos:
        print(" A matrícula {} já esta no cadastro".format(matr))
        continue
    dicItem = {}
    dicItem['nome'] = input(" nome:")
    dicItem['idade'] = int(input(" Idade: "))
    dicItem['curso'] = input(" Curso: ")
    Alunos[matr] = dicItem
print("Fim da leitura de dados\n")

print("Cadastro de Alunos")
for matricula, dados in Alunos.items():
    print(" Aluno {}".format(dados['nome']))
    print("   nºmatr {}".format(matricula))
    print("    idade {}".format(dados['idade']))
    print("    curso {}".format(dados['curso']))
print('*' * 20)
print("Fim do programa")


