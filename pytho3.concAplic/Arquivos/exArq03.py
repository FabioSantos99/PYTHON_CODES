TotGeral = 0
for S in open("Arquivo.txt", "r"):
    S = S.rstrip()
    L = S.split(",")
    L[1], L[2] = int(L[1]), float(L[2])
    TotProd = L[1] * L[2]
    TotGeral += TotProd
    print(" {0:>12}: {1:3} x{2:6.2f) = {3:7.2f}".format(L[0], L[1], L[2], TotProd))
print("-" * 38)
print("Total da Lista de Compras {0:>10}".format(TotGeral))