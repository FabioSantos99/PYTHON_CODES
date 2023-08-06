from tkinter import *
from tkinter import ttk
#cores

cor1 = "#feffff" #white/Branca
cor2 = "#40E51F"
cor3 = "#691EE4"
cor4 = "#11C68B" #laranja

fundo = "#3b3b3b" #fundo preto

janela = Tk()
janela.title("Calculadora")
janela.geometry("238x315")
janela.config(bg=cor4)
photo = PhotoImage(file="calculator.png")
janela.wm_iconphoto(False, photo)


#Frame

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=280)

frame_tela = Frame(janela, width=300, height=56,bg=cor2,pady=0,padx=0, relief="flat",)
frame_tela.grid(row=1, column=0, sticky=NW)

frame_quadros = Frame(janela, width=300, height=340,bg=fundo, pady=0, padx=0, relief="flat",)
frame_quadros.grid(row=2, column=0, sticky=NW)

#_________________FUNÇÕES_____________________--

# Armazenar expressões que serão avaliadas.
todos_valores = ""

# para entrada de valor único
valor_texto = StringVar()
#
# #--------------------------------FUNÇOES----------------------------------------------
#
def entrar_valor(event):
    global todos_valores

    todos_valores = todos_valores + str(event)

    #passar valores para tela
    valor_texto.set(todos_valores)

def calcular():
    global todos_valores
    resultado = str(eval(todos_valores))
    valor_texto.set(resultado)
    todos_valores =""

def limpar_tela():
    global todos_valores
    todos_valores = " "
    valor_texto.set("")


# Criando Label

app_label = Label(frame_tela, text='123456789', width=16, height=2, padx=7, relief=FLAT,anchor= "e", justify=RIGHT, font=('Ivy 13 bold '))
app_label.place(x=45, y=45)


# ------------------------------------- Botões ---------------------------------
b_1 = Button(frame_quadros, text="C", width=19, height=4, bg=cor3,
             fg=fundo,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_quadros, text="%", width=5, height=4, bg=cor3,
             fg=fundo,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_quadros, text="/", width=5, height=4, bg=cor4,
             fg=cor1,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_quadros, text="7", width=5, height=4, bg=cor3,
             fg=fundo,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_quadros, text="8", width=5, height=4, bg=cor3,
             fg=fundo,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_quadros, text="9", width=5, height=2, bg=cor3,
             fg=fundo,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_quadros, text="*", width=5, height=2, bg=cor4,
             fg=cor1,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_7.place(x=177, y=52)

b_8 = Button(frame_quadros, text="4", width=5, height=2, bg=cor3,
             fg=fundo,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_quadros, text="5", width=5, height=2, bg=cor3,
             fg=fundo,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_quadros, text="6", width=5, height=2, bg=cor3,
             fg=fundo,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_quadros, text="-", width=5, height=2, bg=cor4,
             fg=cor1,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_11.place(x=177, y=104)

b_12 = Button(frame_quadros, text="1", width=5, height=2, bg=cor3,
             fg=fundo,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_quadros, text="2", width=5, height=2, bg=cor3,
             fg=fundo,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_quadros, text="3", width=5, height=2, bg=cor3,
             fg=fundo,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_quadros, text="+", width=5, height=2, bg=cor4,
             fg=cor1,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_15.place(x=177, y=156)

b_16 = Button(frame_quadros, text="0", width=11, height=2, bg=cor3,
             fg=fundo,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_quadros, text=".", width=5, height=2, bg=cor3,
             fg=fundo,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(frame_quadros, text="=", width=5, height=2, bg=cor4,
             fg=cor1,font=("Ivy 13 bold"),relief=RAISED,overrelief=RIDGE)
b_18.place(x=177, y=208)


app_scream = Label(frame_tela,textvariable=valor_texto,width=16,height=2,
                   padx=7, relief=FLAT, anchor="e",bd=0,justify=RIGHT,
                   font=('Ivy 18 '), bg='#37474F', fg=cor1)
app_scream.place(x=0,y=0)


#--------------------------------BOTÕES------------------------------------

b_1 = Button(frame_quadros,command = lambda: limpar_tela(), text="C",
             width=11, height=2, bg=cor3, fg=fundo,font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_quadros,command = lambda: entrar_valor('%'), text="%",
             width=5, height=2, bg=cor3, fg=fundo,font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_quadros,command = lambda: entrar_valor('/'), text="/",
             width=5, height=2, bg=cor4, fg=cor1,font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_quadros,command = lambda: entrar_valor('7'), text="7",
             width=5, height=2, bg=cor3, fg=fundo,font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_quadros,command = lambda: entrar_valor('8'), text="8",
             width=5, height=2, bg=cor3, fg=fundo,font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_quadros,command = lambda: entrar_valor('9'), text="9",
             width=5, height=2, bg=cor3, fg=fundo,font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_quadros,command = lambda: entrar_valor('*'), text="*",
             width=5, height=2, bg=cor4, fg=cor1,font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)


b_8 = Button(frame_quadros,command = lambda: entrar_valor('4'), text="4",
             width=5, height=2, bg=cor3, fg=fundo,font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_quadros,command = lambda: entrar_valor('5'), text="5",
             width=5, height=2, bg=cor3, fg=fundo,font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_quadros,command = lambda: entrar_valor('6'), text="6",
             width=5, height=2, bg=cor3, fg=fundo,font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_quadros,command = lambda: entrar_valor('-'), text="-",
             width=5, height=2, bg=cor4, fg=cor1,font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)


b_12 = Button(frame_quadros,command = lambda: entrar_valor('1'), text="1",
             width=5, height=2, bg=cor3, fg=fundo,font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_quadros,command = lambda: entrar_valor('2'), text="2",
             width=5, height=2, bg=cor3, fg=fundo,font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_quadros,command = lambda: entrar_valor('3'), text="3",
             width=5, height=2, bg=cor3, fg=fundo,font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_quadros,command = lambda: entrar_valor('+'), text="+",
             width=5, height=2, bg=cor3, fg=fundo,font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)


b_16 = Button(frame_quadros,command = lambda: entrar_valor('0'), text="0",
             width=11, height=2, bg=cor3, fg=fundo,font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_quadros,command = lambda: entrar_valor('.'), text=".",
             width=5, height=2, bg=cor3, fg=fundo,font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(frame_quadros,command = lambda: entrar_valor('='), text="=",
             width=5, height=2, bg=cor3, fg=fundo,font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)

#Função Calcular -------------------------------------------------------------------------------------------------------------------------

b_18 = Button(frame_quadros,command = lambda: calcular(), text="=", width=5, height=2, bg=cor4, fg=cor1,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)


b_1 = Button(frame_quadros,command = lambda: limpar_tela(), text="C", width=11, height=2, bg=cor3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)

janela.mainloop()




