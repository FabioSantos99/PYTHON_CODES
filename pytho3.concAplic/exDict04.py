Alunos = {}

print("Leitura dos dados")

while True:
    matr = int(input('  Digite a matrícula: '))
    if matr == 0:
        break
    elif matr in Alunos:
        print('A matricula {} já está no cadastro'.format(matr))
        continue
    nome = input(" Nome: ")
    idade = int(input(' Idade: '))
    curso = input(' Curso: ')
    Alunos[matr] = (nome, idade, curso)
print("Fim da leitura de dados\n")

print('Cadastro de Alunos')
for matricula, dados in Alunos.items():
    print(" Aluno {}".format(dados[0]))
    print("   nºmatr {}".format(matricula))
    print("   idade  {}".format(dados[1]))
    print("   curso  {}".format(dados[2]))
print('\nFim do programa')



