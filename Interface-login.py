from tkinter import *
from tkinter import simpledialog

entrada_admin = False
entress = 0

class Application:

    #entrada_admin = False

    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer["background"] = base
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer["background"] = base
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer["background"] = base
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer["background"] = base
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Dados do usuário", background=base)
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao, background=base)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao, background=base)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "12")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()



        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao, background=base)
        self.mensagem.pack()

    #Método verificar senha
    def verificaSenha(self):
        global entress
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "dev" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
            entress = 1
            t(janela)
        else:
            self.mensagem["text"] = "Erro na autenticação"

    print(entress)


class t:
    def __init__(self, master=None):
        # texto = Label(janela, text="texto teste")
        # texto.grid(column=0, row=0, padx=30, pady=4)
        # texto.configure(background=base)

        self.texto = Label(janela, text="texto teste")
        self.texto.grid(column=0, row=0, padx=30, pady=4)
        self.texto["background"] = base

        # texto_resposta = Label(janela, text="a", background=base)
        # texto_resposta.grid(column=0, row=2, padx=10, pady=10)

        self.texto_resposta = Label(janela, text="a", background=base)
        self.texto_resposta["background"] = base
        self.texto_resposta.grid(column=0, row=2, padx=10, pady=10)

        # botao = Button(janela, text="Insira aqui a ação do seu botão", command=tt)
        # botao.grid(column=0, row=1, padx=10, pady=10)

        self.botao = Button(janela, text="Insira aqui a ação do seu botão")
        self.botao["text"] = "coloca texto"
        self.botao["command"] = self.tt
        self.botao.grid(column=0, row=1, padx=10, pady=10)

    def tt(self):
        self.texto_resposta.configure(text="teste")










base = "#738991"

janela = Tk()
janela.title("Teste")
janela.geometry("600x500")
janela.configure(background=base)

#texto = Label(janela, text="texto teste")
#texto.grid(column=0, row=0, padx=30, pady=4)
#texto.configure(background=base)
Application(janela)





janela.mainloop()