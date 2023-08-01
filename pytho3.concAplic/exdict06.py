print('primeiro conjunto')
print('-' * 40)

frutas1 = set()
x = input('Digite dados do primeiro conjunto: ')

while x != 'fim':
    frutas1.add(x)
    x = input('Digite dados do primeiro conjunto: ')

    ###############

print("Dados do segundo conjunto")
frutas2 = set()
x = input('Digite dados do segundo conjunto: ')
while x != 'fim':
    frutas2.add(x)
    x = input('Digite dados do segundo conjunto: ')
print("Conjunto 1: {}".format(frutas1))
print("Conjunto 2: {}".format(frutas2))
print("União de frutas1 e frutas2")
print(frutas1 | frutas2)
print('Interseçao de frutas 1 e 2')
print(frutas1 & frutas2)




