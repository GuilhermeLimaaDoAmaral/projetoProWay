def linha(tam = 42):
    return "-" * tam



def LeiaResp(msg):
    while True:
        try:
            wNum = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro válido.\033[m')
            break
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            break
        else:
            return wNum

def LeiaFloat(msg):
    while True:
        try:
            wNum = float(msg)
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número válido.\033[m')
            break
        else:
            return wNum

def LeiaString(msg):
    while True:
        try:
            wNum = str(msg)
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite seu nome.\033[m')
            wNum = ""
            return wNum
            break
        else:
            return wNum


def contaLinha(lista):
    wC = 1
    for wI in range(0, len(lista)):
        print(wC, " - ", lista[wI])
        wC = wC + 1
    print(linha())


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menuRel(lista):
    cabecalho("RELATÓRIOS")
    contaLinha(lista)

    opc = LeiaResp("Sua opção: ")
    return opc


def menu(lista):
    cabecalho("OPÇÕES")
    contaLinha(lista)

    opc = LeiaResp("Sua opção: ")
    return opc

def PreencheADireita(Texto : str, prTamanho : int):
    return Texto.ljust(prTamanho, " ")


def PreencheAEsquerda(Texto : str, prTamanho : int):
    return float(Texto.rjust(prTamanho,"0"))