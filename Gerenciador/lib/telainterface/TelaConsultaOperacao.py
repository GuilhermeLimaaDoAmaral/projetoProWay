from functools import partial
from tkinter import *
from tkinter import ttk
import os
import re
from Gerenciador.lib.telainterface import *
import ctypes

pastaApp = os.path.dirname(__file__)


def setaCabecalho(pTreeView):
    pTreeView.grid_remove()
    pTreeView.column('nome', minwidth=0, width=100)
    pTreeView.heading("nome", text='Cadastro')

    pTreeView.column('moedaOri', minwidth=0, width=90)
    pTreeView.heading("moedaOri", text='Moeda origem')

    pTreeView.column('moedaDest', minwidth=0, width=90)
    pTreeView.heading("moedaDest", text='Moeda destino')

    pTreeView.column('dataOp', minwidth=0, width=90)
    pTreeView.heading("dataOp", text='Data operacao')

    pTreeView.column('valorOri', minwidth=0, width=80)
    pTreeView.heading("valorOri", text='Valor origem')

    pTreeView.column('valorconv', minwidth=0, width=100)
    pTreeView.heading("valorconv", text='Valor convertido')

    pTreeView.column('valorTaxa', minwidth=0, width=50)
    pTreeView.heading("valorTaxa", text='Taxa')

    pTreeView.place(relx=8.81, rely=0.95, relheight=8.85)

    pTreeView.grid(column=0, row=3, columnspan=3, pady=10)

def delete(prTreeView):
    itemSelecionado = prTreeView.selection()[0]
    prTreeView.delete(itemSelecionado)
    wArq = open('C:\\Users\\User\\PycharmProjects\\ProWay\\Gerenciador\\lib\\telainterface\\CadastroDeOperacao.txt',
                'r+')
    wLinha = wArq.readlines()
    wLinha[int(itemSelecionado.replace("I",""), 16) - 1] = ""
    wArq.close()

    os.remove('C:\\Users\\User\\PycharmProjects\\ProWay\\Gerenciador\\lib\\telainterface\\CadastroDeOperacao.txt')

    try:
        a = open('CadastroDeOperacao.txt', 'wt+')
        a.close()
    except:
        print("Houve um erro na criação do arquivo!")

    wArq = open('C:\\Users\\User\\PycharmProjects\\ProWay\\Gerenciador\\lib\\telainterface\\CadastroDeOperacao.txt',
                'r+')

    wArq.writelines(wLinha)

    #setaCabecalho(prTreeView)

    #for wLinha in wArq:
    #    wLinha = wLinha.rstrip()
    #
    #    wLinha = wLinha.split(";")
    #    prTreeView.insert("", "end",
    #                      values=(wLinha[0], wLinha[1], wLinha[2], wLinha[3], wLinha[4], wLinha[5], wLinha[6]))
    wArq.close()

wTela: Tk = Tk()
wTela.title("Consulta de operacoes")
wTela.geometry("750x245")
wCorback = "#87CEEB"
wTela.configure(background=wCorback)

wTreeView = ttk.Treeview(wTela, height=10,
                         columns=('nome', 'moedaOri', 'moedaDest', 'dataOp', 'valorOri', 'valorconv', 'valorTaxa'),
                         show='headings')

setaCabecalho(wTreeView)

scrolLista = Scrollbar(wTela, orient='vertical')
wTreeView.configure(yscroll=scrolLista.set)
scrolLista.place(relx=0.96, rely=0, relwidth=0.04, relheight=1)

wTreeView.grid(column=0, row=3, columnspan=3, pady=10)

btLimpar = Button(wTela, text="Excluir")

btLimpar["command"] = partial(delete, wTreeView)

btLimpar.place(x=610, y=11, width=60, height=20)

wArq = "CadastroDeOperacao.txt"

if not ExisteArquivo:
    CriaArquivo(wArq)

wArq = open('C:\\Users\\User\\PycharmProjects\\ProWay\\Gerenciador\\lib\\telainterface\\CadastroDeOperacao.txt', 'r')

for wLinha in wArq:
    wLinha = wLinha.rstrip()

    wLinha = wLinha.split(";")
    wTreeView.insert("", "end", values=(wLinha[0], wLinha[1], wLinha[2], wLinha[3], wLinha[4], wLinha[5], wLinha[6]))

wArq.close()

wTela.mainloop()
