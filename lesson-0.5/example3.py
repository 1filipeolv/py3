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
tela.mainloop()