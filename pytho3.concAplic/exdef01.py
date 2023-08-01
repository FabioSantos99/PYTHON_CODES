def imparPar(x):
    R = x % 2
    print(R)

    if R == 0:
       print ("resultado é par")
    else:
        print("Resultado é impar")

a = int(input("Digite um valor para a: "))
s = imparPar(a)
