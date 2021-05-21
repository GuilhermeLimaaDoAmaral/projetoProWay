from tkinter import *
from Comandos import*

#from tkinter import ttk
def TelaGerenciadorOperacao():
    wCorback = "#E6E6FA"
    wTela: Tk = Tk()
    photo = PhotoImage(file = "image/telainicial.png")
    label = Label(wTela, image= photo)
    label.pack()


    #width_value  = wTela.winfo_screenwidth()
    #height_value = wTela.winfo_screenheight()

    wTela.title("Gerenciador de operações")
    wTela.geometry("%dx%d+0+0" % (1358, 616))
    wTela.configure(background=wCorback)

    wBarraMenu = Menu(wTela)
    wCadastros = Menu(wBarraMenu, tearoff=0)
    wCadastros.add_command(label="Cadastro de operações", command=ComandoAbreTelaCadOperacao)
    wBarraMenu.add_cascade(label="Cadastros", menu=wCadastros)

    wConsultas = Menu(wBarraMenu, tearoff=0)
    wConsultas.add_command(label="Consulta das operações", command=ComandoAbreTelaConsultaOperacao)
    wBarraMenu.add_cascade(label="Consultas", menu=wConsultas)

    wRelatorios = Menu(wBarraMenu, tearoff=0)
    wRelatorios.add_command(label="Lista de operações ", command=ComandoAbreTelaRelatorioOperacao)
    wRelatorios.add_command(label="Valor total das operações ", command="")
    wRelatorios.add_command(label="Valor total das taxas cobradas ", command="")
    wBarraMenu.add_cascade(label="Relatorios", menu=wRelatorios)

    wTela.config(menu=wBarraMenu)
    wTela.mainloop()


   # wOpcoes.add_command(label="Consulta das operações", command=Comando())
   # wOpcoes.add_command(label="Gerar relatórios de operações", command=Comando())
   #wOpcoes.add_command(label="Sair do sistema", command=wTela.quit)
   #   wOpcoes.add_separator()