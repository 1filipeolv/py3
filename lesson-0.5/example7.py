from tkinter import *

tela = Tk()

txt_nome = Entry(tela, width=20, borderwidth=5, fg="blue", bg="white")
txt_nome.pack()
txt_nome.insert(0,"Digite o seu nome")

btn_botao = Button(tela, text="Click")
btn_botao.pack()

tela.mainloop()