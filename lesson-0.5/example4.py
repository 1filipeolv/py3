from tkinter import *
#criação da variavel
tela = Tk()


#Titulo na barra de tarefas
tela.title("Fatec Registro")
#Configuração da cor da tela (opcional)
tela.configure(background= '#le3743')
#Configuração do tamnho da tela
tela.geometry("700x600")

tela.resizable(True, True)
#Tamanho maximo que atela pode chegar
tela.maxsize(width=800, height=700)
#Tamanho minimo que a tela pode chegar
tela.minsize(width=500, height=300)


lbl_teste = Label(tela, text="TESTE").place (x=10, y=10)
#lbl_teste e o nome de indentificação interno da label
#Label e o tipo do componente
#tela a variavel que a label está ligado
#text="" e o texto a ser exibido na tela
#place o posicionamente da tela
tela.mainloop()