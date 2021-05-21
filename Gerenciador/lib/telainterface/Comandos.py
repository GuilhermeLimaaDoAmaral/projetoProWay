import os

pastaApp = os.path.dirname(__file__)


def Comando():
    print("")


def ComandoAbreTelaCadOperacao():
    exec(open(pastaApp + "\\TelaCadOperacao.py").read())


def ComandoAbreTelaConsultaOperacao():
    exec(open(pastaApp + "\\TelaConsultaOperacao.py").read())


def ComandoAbreTelaRelatorioOperacao():
    exec(open(pastaApp + "\\TelaRelOperacao.py").read())


def ButtonCad():
    print(" ")