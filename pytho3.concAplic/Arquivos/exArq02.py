print("Inicio do Programa")

Soma = 0
Cont = 0

for S in open("Inteiros.txt"):
    N = int(S)
    Soma = Soma + N
    Cont = Cont + 1
    print("elemento {0} = {1}".format(Cont, N))
print("\nSoma = {0}".format(Soma))


print("Fim do Programa")





# arq = open("Inteiros.txt", 'r')
# S = arq.readline()
# while S != "":
#     N = int(S)
#     Soma = Soma + N
#     Cont = Cont + 1
#     print("Elemento {0} = {1}".format(Cont, N))
#     S = arq.readline()
# arq.close()
# print("\nSoma = {0}".format(Soma))



