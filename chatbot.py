# coding=utf-8

from tkinter import *

root = Tk()

def send ():
    send='Você' + a.get()
    text.insert(END,'\n' + send)
    if (a.get() == 'oi'):
        text.insert(END, '\n' + 'Gpteles: Oi, tudo bem?')
    elif(a.get) == ('Olá'):
        text.insert(END, '\n' + 'Gpteles: Olá, tudo bem?')
    elif(a.get) == ('Qual o maior time do nordeste?'):
        text.insert(END, '\n' + 'Gpteles: é o BAHIA!!')
    elif(a.get) == ('que dia é hoje?'):
        text.insert(END, '\n' + 'Gpteles: Dia de tomar uma')
    elif(a.get) == ('qual time você torce?'):
        text.insert(END, '\n' + 'Gpteles: BBMP!!')

text = Text(root, bg='white')
text.grid(row=0, column=0, columnspan=2)

a = Entry (root, width=40) 

send = Button(root, text = 'Enviar', bg='white', width = 20, command =send).grid(row = 1, column = 1)

 # DEFININDO BOTÃO DE ENVIAR, TAMANHO E COR
a.grid(row=1, column = 0)

root.title('ChatGPTELES')

root.mainloop
