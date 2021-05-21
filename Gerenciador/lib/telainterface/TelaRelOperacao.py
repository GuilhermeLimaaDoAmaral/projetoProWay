from tkinter import *
from tkinter import ttk
import os

pastaApp = os.path.dirname(__file__)


def Busca():
    print("")


wTela: Tk = Tk()
wTela.title("Lista de operacao")
wTela.geometry("750x238")
wCorback = "#87CEEB"
wTela.configure(background=wCorback)

wTreeView = ttk.Treeview(wTela, height=10,columns=('nome', 'moedaOri', 'moedaDest', 'dataOp', 'valorOri', 'valorconv', 'valorTaxa', 'valorope'),
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


wTreeView.column('valorope', minwidth=0, width=110)
wTreeView.heading("valorope", text='Valor da operação')

wTreeView.place(relx=8.81, rely=0.95, relheight=8.85)

scrolLista = Scrollbar(wTela, orient='vertical')
wTreeView.configure(yscroll=scrolLista.set)
scrolLista.place(relx=0.96, rely=0, relwidth=0.04, relheight=1)

wTreeView.grid(column = 0, row = 3, columnspan = 3, pady = 10)

wArq = open('C:\\Users\\User\\PycharmProjects\\ProWay\\Gerenciador\\lib\\telainterface\\CadastroDeOperacao.txt', 'r')

for wLinha in wArq:
    wLinha = wLinha.rstrip()

    wLinha = wLinha.split(";")
    wTreeView.insert("", "end", values = (wLinha[0], wLinha[1], wLinha[2], wLinha[3], wLinha[4], wLinha[5], wLinha[6]))

wArq.close()

wTela.mainloop()
