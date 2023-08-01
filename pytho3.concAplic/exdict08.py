# EXERCICIO 3 DO CAPITULO 6 DO LIVRO

Num = set()
cont = 0

while True:
    x = int(input("Digite um valor: "))

    if x <= 0:
        break

    else:
        Num.add(x)
        cont += 1

print('Total de numeros gerado {} = {}'.format(cont, Num))


