from tkinter import *

janela = Tk()
janela.title("Criando uma entry Entry")
janela.geometry("300x300")

label_nome = Label(janela, text="Nome")
label_nome.grid(row=0, column=0)
nome = Entry(janela, width= 20)
nome.grid(row=0, column=1)

label_idade = Label(janela, text="Idade")
label_idade.grid(row=1, column=0)
idade = Entry(janela, width= 20)
idade.grid(row=1, column=1)

label = Label(janela, text="Pais")
label.grid(row=2, column=0)
pais = Entry(janela, width= 20)
pais.grid(row=2, column=1)

def botton():
    n = nome.get()
    i = idade.get()
    p = pais.get()

    label = Label(janela, text=n + " " + i +" "+ p)
    label.grid(row=6,column=1)
    print(n, i, p)

b = Button(janela, text="Clicar", bg="white", command=botton)
b.grid(row=4, column=0)



janela.mainloop()