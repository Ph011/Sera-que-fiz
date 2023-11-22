import tkinter
from tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
import time

janela = Tk()
janela.geometry("1035x314")
janela.configure(background='#1E1E1E')
janela.title('Sera que fiz | ph011')
janela.iconbitmap('img/logo.ico')

macaco = Canvas(janela,width=300, height=300, background='#1E1E1E')
macaco.pack()

img = ImageTk.PhotoImage(Image.open("img/masqueico.jpg"))
macaco.create_image(150,150,image=img)
macaco.place(x=5,y=5)

versao = Label(text='V0.0.0',background='#1E1E1E', foreground='white',font='Century 6')
versao.place(x=320,y=20)

titulo = Label(text="Será que fiz ?", font='Century 25', background='#1E1E1E', foreground='white')
titulo.place(x=380,y=0)

autor = Label(text='By ph011', background='#1E1E1E', foreground='white',font='Century 6')
autor.place(x=590,y=20)

data = datetime.now()
horario = data.strftime('   %d/%m/%Y %H:%M')
dataatt = Label(janela, text=horario,background='#1E1E1E', foreground='white',font='15')
dataatt.place(x=890,y=25)
hora = data.hour

def limpezaDeTxt():
    if (hora == 19):
        with open('fiz.txt', 'w') as limpo:
            limpo.truncate(0)

if (hora <= 7):
    print('Está na hora de limpar o txt')
    limpezaDeTxt()
else:
    print('não está na hora de limpar o txt')


caixa = tkinter.Listbox(width=63, height=11)
caixa.place(x=650,y=50)


def confirmar0():
    caixa.insert(END,'✓ '+tarefaslist[0] + horario)
    arquivotxt = open('fiz.txt', "a")
    arquivotxt.write('OK! {}{}\n'.format(tarefaslist[0],horario))
    arquivotxt.close()
    print('Item 0 Adicionado no txt')
def confirmar1():
    caixa.insert(END,'✓ '+tarefaslist[1] + horario)
    arquivotxt = open('fiz.txt', "a")
    arquivotxt.write('OK! {}{}\n'.format(tarefaslist[1],horario))
    arquivotxt.close()
    print('Item 1 Adicionado no txt')
def confirmar2():
    caixa.insert(END,'✓ '+tarefaslist[2] + horario)
    arquivotxt = open('fiz.txt', "a")
    arquivotxt.write('OK! {}{}\n'.format(tarefaslist[2],horario))
    arquivotxt.close()
    print('Item 2 Adicionado no txt')
def confirmar3():
    caixa.insert(END,'✓ '+tarefaslist[3] + horario)
    arquivotxt = open('fiz.txt', "a")
    arquivotxt.write('OK! {}{}\n'.format(tarefaslist[3],horario))
    arquivotxt.close()
    print('Item 3 Adicionado no txt')

tarefaslist = ['Tomar banho', 'Raspar o suvaco', 'Tirar remela do olho', 'Ensinar o papagaio a cantar o hino do Palmeiras']

feito0 = Button(text='✓', command=confirmar0)
feito0.place(x=320, y=50)
tarefa0 = Label(text=tarefaslist[0], background='#1E1E1E',foreground='white',font='Helvetica 10')
tarefa0.place(x=350,y=50)

feito1 = Button(text='✓',command=confirmar1)
feito1.place(x=320, y=100)
tarefa1 = Label(text=tarefaslist[1],background='#1E1E1E', foreground='white',font='Helvetica 10')
tarefa1.place(x=350,y=100)

feito2 = Button(text='✓',command=confirmar2)
feito2.place(x=320, y=150)
tarefa2 = Label(text=tarefaslist[2],background='#1E1E1E', foreground='white',font='Helvetica 10')
tarefa2.place(x=350,y=150)

feito3 = Button(text='✓', command=confirmar3)
feito3.place(x=320, y=200)
tarefa3 = Label(text=tarefaslist[3],background='#1E1E1E', foreground='white',font='Helvetica 10')
tarefa3.place(x=350,y=200)

sair = Button(text='SALVAR E SAIR', command=janela.destroy,background='red', foreground='white', font='15')
sair.place(x=899, y=235)


janela.mainloop()
print('Fechando...')