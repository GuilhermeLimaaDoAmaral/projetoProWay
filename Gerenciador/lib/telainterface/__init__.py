from Gerenciador.lib.interface import *

def ExisteArquivo(nome):
    try:
        a = open(nome, 'rt')
        a.close()
        return True
    except FileNotFoundError:
        return False


def CriaArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Houve um erro na criação do arquivo!")

def CadastrarOperacoes(prNomeArq, prEdNome : str, prEdMoedaOri : str, prEdMoedaDest : str, prEdDataOper : str,
                       prEdValorOri : str, prEdValorDest : str, prEdTaxa : str):

    wNome      = prEdNome
    wMoedaOri  = prEdMoedaOri
    wMoedaDest = prEdMoedaDest
    wDataOper  = prEdDataOper
    wValorOri  = prEdValorOri
    wValorConv = prEdValorDest
    wValorTaxa = prEdTaxa

    LeiaString(wNome)
    LeiaString(wMoedaOri)
    LeiaString(wMoedaDest)
    LeiaString(wDataOper)

    LeiaFloat(wValorOri)
    LeiaFloat(wValorConv)
    LeiaFloat(wValorTaxa)

    wNome      = PreencheADireita(wNome, 19)
    wMoedaOri  = PreencheADireita(wMoedaOri, 17)
    wMoedaDest = PreencheADireita(wMoedaDest, 17)
    wDataOper  = PreencheADireita(wDataOper, 17)

    wValorOri  = PreencheAEsquerda(float.__str__(wValorOri), 17)
    wValorConv = PreencheAEsquerda(float.__str__(wValorConv), 17)
    wValorTaxa = PreencheAEsquerda(float.__str__(wValorTaxa), 17)

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
            print("Cadastro efetuado com sucesso.")
            a.close()


def LerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Erro ao abrir o arquivo")
    else:
        cabecalho("Operações cadastradas")
        print(a.read())
    finally:
        a.close()