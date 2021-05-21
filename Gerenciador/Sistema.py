from Gerenciador.lib.telainterface import*
from time import sleep

wArq = "CadastroDeOperacoes.txt"

if not ExisteArquivo(wArq):
    CriaArquivo(wArq)

while True:
    wResposta = menu(["Cadastro de operações", "Consulta das operações","Gerar relatórios de operações", "Sair do sistema"])

    if wResposta == 1:
        CadastrarOperacoes(wArq)
    elif wResposta == 2:
        LerArquivo(wArq)
    elif wResposta == 3:
        print("Implementar os relatórios")
    elif wResposta == 4:
        print("Saindo do sistema...")
        break
    else:
        print("Digite uma opção válida!")

    sleep(2)

    #menuRel(["Lista de operações", "Valor total das operações", "Valor total das taxas cobradas"])
