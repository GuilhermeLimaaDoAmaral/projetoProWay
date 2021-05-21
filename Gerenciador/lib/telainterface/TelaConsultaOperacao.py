from functools import partial
from tkinter import *
from tkinter import ttk
import os

pastaApp = os.path.dirname(__file__)


def converteStrParaInt(itemSelecionado):
    wLinha = int(itemSelecionado[1] + itemSelecionado[2] + itemSelecionado[3]) - 1
    return wLinha

def delete(prTreeView):
    #print(len(prTreeView))
    itemSelecionado = prTreeView.selection()[0]
    prTreeView.delete(itemSelecionado)
    wArq = open('C:\\Users\\User\\PycharmProjects\\ProWay\\Gerenciador\\lib\\telainterface\\CadastroDeOperacao.txt','r+')
    wLinha = wArq.readlines()
    #wLinha[converteStrParaInt(itemSelecionado)]
    wLinha[int(itemSelecionado[1] + itemSelecionado[2] + itemSelecionado[3]) - 1] = ""
    wArq.close()

    os.remove('C:\\Users\\User\\PycharmProjects\\ProWay\\Gerenciador\\lib\\telainterface\\CadastroDeOperacao.txt')

    try:
        a = open('CadastroDeOperacao.txt', 'wt+')
        a.close()
    except:
        print("Houve um erro na criação do arquivo!")

    wArq = open('C:\\Users\\User\\PycharmProjects\\ProWay\\Gerenciador\\lib\\telainterface\\CadastroDeOperacao.txt', 'r+')
    wArq.writelines(wLinha)


wTela: Tk = Tk()
wTela.title("Consulta de operacoes")
wTela.geometry("750x245")
wCorback = "#87CEEB"
wTela.configure(background=wCorback)

wTreeView = ttk.Treeview(wTela, height=10,columns=('nome', 'moedaOri', 'moedaDest', 'dataOp', 'valorOri', 'valorconv', 'valorTaxa'),
                    show='headings')

wTreeView.column('nome', minwidth=0, width=100)
wTreeView.heading("nome", text='Cadastro')

wTreeView.column('moedaOri', minwidth=0, width=90)
wTreeView.heading("moedaOri", text='Moeda origem')

wTreeView.column('moedaDest', minwidth=0, width=90)
wTreeView.heading("moedaDest", text='Moeda destino')

wTreeView.column('dataOp', minwidth=0, width=90)
wTreeView.heading("dataOp", text='Data operacao')

wTreeView.column('valorOri', minwidth=0, width=80)
wTreeView.heading("valorOri", text='Valor origem')

wTreeView.column('valorconv', minwidth=0, width=100)
wTreeView.heading("valorconv", text='Valor convertido')

wTreeView.column('valorTaxa', minwidth=0, width=50)
wTreeView.heading("valorTaxa", text='Taxa')

wTreeView.place(relx=8.81, rely=0.95, relheight=8.85)

scrolLista = Scrollbar(wTela, orient='vertical')
wTreeView.configure(yscroll=scrolLista.set)
scrolLista.place(relx=0.96, rely=0, relwidth=0.04, relheight=1)

wTreeView.grid(column = 0, row = 3, columnspan = 3, pady = 10)


#btLimpar= Button(wTela, text="Excluir", command = delete(wTreeView))
btLimpar= Button(wTela, text="Excluir")
btLimpar["command"] = partial(delete, wTreeView)
btLimpar.place(x=610, y=11, width=60, height=20)

#lbIcone = Label(wTela,background=wCorback)
#lbIcone.place(x=610, y=130, width=100, height=110)

#photo1 = PhotoImage(file="image\IconeTela.png")
#label = Label(lbIcone, image=photo1)
#label.pack()



wArq = open('C:\\Users\\User\\PycharmProjects\\ProWay\\Gerenciador\\lib\\telainterface\\CadastroDeOperacao.txt', 'r')

for wLinha in wArq:
    wLinha = wLinha.rstrip()

    wLinha = wLinha.split(";")
    wTreeView.insert("", "end", values = (wLinha[0], wLinha[1], wLinha[2], wLinha[3], wLinha[4], wLinha[5], wLinha[6]))

wArq.close()

wTela.mainloop()
