import GerStoque
import GerClientes
import GerCaixa

def Sis_loja():
    while True:
        print('-'  *30)
        print('SISTEMA DE GESTÃO DE LOJA (SisLoja)')
        print('Gestão de estoque (1)')
        print('Gestão de clientes (2)')
        print('Gestão de fluxo (3)')
        print('APERTE 0 PARA ENCERRAR O PROGRAMA')
        print('-'*30)
        pergunta = int(input('Selecionar a opção desejada: '))
        if pergunta == 1:
            GerStoque.Gerstoque()
        elif pergunta == 2:
            GerClientes.Gercliente()
        elif pergunta == 3:
            GerCaixa.Gercaixa()
        elif pergunta == 0:
            break
Sis_loja()
           

