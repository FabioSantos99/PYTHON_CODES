from random import randint
from tkinter import *

janela = Tk()
janela.title("Guess Number")
janela.geometry("350x150")
janela.config(bg="blue")

label_ask = Label(janela, bg="blue", text= "Digite um número de 0 à 50:")
label_ask.grid(row=0, column=2)
ask = Entry(janela,width=20)
ask.grid(row=1,column=2)

# num = 0
# chances = 10
#
# while True:
#     random = randint(0, 8)
#     num = int(input("Digite um numero de 0 à 50: "))
#     if num == random:
#         print("O numero é {}, parabens você acertou.".format(random))
#         random = randint(0, 8)
#         chances = 10
#         num = int(input("Digite um numero de 0 à 50: "))
#
#     else:
#         if num > random:
#             chances -= 1
#             print('digite um numero menor. Vc tem {} chances'.format(chances))
#
#         elif num < random:
#             chances -= 1
#             print('digite um numero maior. Vc tem {} chances'.format(chances))
#
#         if chances == 0:
#             print('')
#             print('Vc Perdeu')
#             break

janela.mainloop()





