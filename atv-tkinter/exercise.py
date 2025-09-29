import tkinter as tk

# Cria a janela principal
janela = tk.Tk()
janela.title("Sistema de Cadastro Familiar")
janela.geometry("600x500")

def verifica_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

def atualizar_tela():
    lbl_resultado.config(text="")
    texto = ""
    for f in lista_familiares:
        status = verifica_idade(f["idade"])
        # Verifica se pode votar
        if f["idade"] >= 16:
            voto = "Pode votar"
        else:
            voto = "Nao pode votar"
        texto += f"{f['nome']} | Idade: {f['idade']} ({status}) | Celular: {f['celular']} | Parentesco: {f['parente']} | CPF: {f['cpf']} | Cidade: {f['local']} | {voto}\n"
    lbl_resultado.config(text=texto)

# Titulo da tela
tk.Label(janela, text="Cadastro Familiar", font=("Arial", 16)).pack(pady=10)

# Campo nome
tk.Label(janela, text="Nome").pack()
campo_nome = tk.Entry(janela)
campo_nome.pack()

# Campo idade
tk.Label(janela, text="Idade").pack()
campo_idade = tk.Entry(janela)
campo_idade.pack()

# Campo celular
tk.Label(janela, text="celular").pack()
campo_celular = tk.Entry(janela)
campo_celular.pack()

# Campo parentesco
tk.Label(janela, text="Parentesco").pack()
campo_parente = tk.Entry(janela)
campo_parente.pack()

# Campo cpf
tk.Label(janela, text="CPF").pack()
campo_cpf = tk.Entry(janela)
campo_cpf.pack()

# Campo cidade
tk.Label(janela, text="Cidade").pack()
campo_local = tk.Entry(janela)
campo_local.pack()

# Dados familiares
lista_familiares = [
    {"nome": "Filipe", "idade": 20, "celular": "13996182430", "parente": "Eu mesmo", "cpf": "444.544.111-43", "local": "Registro-SP"},
    {"nome": "Ivani", "idade": 46, "celular": "13996540771", "parente": "Mae", "cpf": "123.456.789-00", "local": "Registro-SP"},
    {"nome": "Herbert", "idade": 53, "celular": "13997844229", "parente": "Pai", "cpf": "987.654.321-00", "local": "Registro-SP"},
    {"nome": "João", "idade": 11, "celular": "13997391280", "parente": "Irmao", "cpf": "111.222.333-44", "local": "Registro-SP"}
]

# Label pra mostrar os resultados
lbl_resultado = tk.Label(janela, text="", justify="left", anchor="w")
lbl_resultado.pack()

# Chama a funcao pra mostrar os dados iniciais
atualizar_tela()

def cadastrar():
    nome = campo_nome.get()
    idade = int(campo_idade.get())
    celular = campo_celular.get()
    parente = campo_parente.get()
    cpf = campo_cpf.get()
    local = campo_local.get()
    novo = {
        "nome": nome,
        "idade": idade,
        "celular": celular,
        "parente": parente,
        "cpf": cpf,
        "local": local
    }
    lista_familiares.append(novo)
    atualizar_tela()

# Botão cadastrar
botao = tk.Button(janela, text="Cadastrar", command=cadastrar)
botao.pack(pady=10)

janela.mainloop()