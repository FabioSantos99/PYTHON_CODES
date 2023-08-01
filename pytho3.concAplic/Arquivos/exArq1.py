arqreais = open('ValsReais.txt', 'w')
x = float(input("Digite um numero real: "))

while x != 0:
    arqreais.write("{0:.2f}\n".format(x))
    x = float(input("Digite um numero real: "))
arqreais.close()

Soma = 0
Cont = 0

for S in open("ValsReais.txt"):
    N = float(S)
    Soma = Soma + N
    Cont += 1
    print("Elemento {0} = {1}".format(Cont,N))
print("\nSoma = {0}".format(Soma))

print("Fim do Programa")
