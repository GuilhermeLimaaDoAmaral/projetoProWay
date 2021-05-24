from tkinter import *
from Gerenciador.lib.telainterface import *
from functools import partial

def Cadastro(prNome: Entry, prMoedaOri: Entry, prMoedaDest: Entry, prDataOper: Entry, prValorOri: Entry,
             prValorConv: Entry, prValorTaxa: Entry, prNomeArq: Entry):

    wNome = prNome.get()
    wMoedaOri = prMoedaOri.get()
    wMoedaDest = prMoedaDest.get()
    wDataOper = prDataOper.get()

    wValorOri = prValorOri.get()
    wValorConv = prValorConv.get()
    wValorTaxa = prValorTaxa.get()

    try:
        a = open(prNomeArq, 'at')
    except:
        print("Houve um erro ao abrir o arquivo")
    else:
        try:
            a.write(f'{wNome}; {wMoedaOri}; {wMoedaDest}; {wDataOper}; {wValorOri}; {wValorConv}; {wValorTaxa}\n')
        except:
            print("Houve um erro ao cadastrar a operação.")
        else:
            print("Cadastrado com sucesso.")
            a.close()


wCorback = "#87CEEB"
wTela: Tk = Tk()
wTela.title("Cadastro de operacoes")
wTela.geometry("500x280")
wTela.configure(background=wCorback)

lbNomeCliente = Label(wTela, text="Nome: ", background=wCorback, foreground="#000000")
lbNomeCliente.place(x=90, y=20, width=40, height=20)

edNomeCliente: Entry = Entry(wTela)
edNomeCliente.place(x=150, y=20, width=100, height=20)

lbMoedaOri = Label(wTela, text="Moeda de origem: ", background=wCorback, foreground="#000000")
lbMoedaOri.place(x=30, y=50, width=100, height=20)

edMoedaOri = Entry(wTela)
edMoedaOri.place(x=150, y=50, width=100, height=20)

lbMoedaDest = Label(wTela, text="Moeda de destino: ", background=wCorback, foreground="#000000")
lbMoedaDest.place(x=30, y=80, width=100, height=20)

edMoedaDest = Entry(wTela)
edMoedaDest.place(x=150, y=80, width=100, height=20)

lbDataope = Label(wTela, text="Data de operacao: ", background=wCorback, foreground="#000000")
lbDataope.place(x=30, y=110, width=100, height=20)

edDataope = Entry(wTela)
edDataope.place(x=150, y=110, width=100, height=20)

lbValorOri = Label(wTela, text="Valor original: ", background=wCorback, foreground="#000000")
lbValorOri.place(x=41.5, y=140, width=100, height=20)

edValorOri = Entry(wTela)
edValorOri.place(x=150, y=140, width=100, height=20)

lbValorConv = Label(wTela, text="Valor convertido: ", background=wCorback, foreground="#000000")
lbValorConv.place(x=33.5, y=170, width=100, height=20)

edValorConv = Entry(wTela)
edValorConv.place(x=150, y=170, width=100, height=20)

lbTaxa = Label(wTela, text="Taxa: ", background=wCorback, foreground="#000000")
lbTaxa.place(x=64.5, y=200, width=100, height=20)

edTaxa = Entry(wTela)
edTaxa.place(x=150, y=200, width=100, height=20)


lbIcone = Label(wTela,background=wCorback)
lbIcone.place(x=300, y=115, width=100, height=110)

#photo3 = PhotoImage(file="image\IconeTela.png")
#label = Label(lbIcone, image=photo3)
#label.pack()


wArq = "CadastroDeOperacao.txt"

if not ExisteArquivo:
    CriaArquivo(wArq)

btCadastro = Button(wTela, text="Cadastrar")
btCadastro["command"] = partial(Cadastro, edNomeCliente, edMoedaOri, edMoedaDest, edDataope,
                                edValorOri, edValorConv, edTaxa, wArq)
btCadastro.place(x=300, y=20, width=60, height=20)

wTela.mainloop()
