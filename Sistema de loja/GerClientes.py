#listas
clientes = list()
lista_cpf = list()
lista_renda = list()
lista_a = list() #lista de cpf com renda menor que 5000
lista_b = list() #lista de cpf com renda entre 5000 e 10000
lista_c = list() #lista de cpf com renda maior que 1000
def Gercliente():
    a = input('DESEJA CADASTRAR UMA NOVO CLIENTE?(S/N)').upper()
    while True:
        if a == 'N' or a == '0' :
            break
        elif a == 'S':
            cpf = str(input('Digite o cpf do cliente: '))
            if cpf == '0':
                print('operação encerrada')
                break
            while len(cpf) != 11 :
                cpf = str((input('digite novamente: ')))
            lista_cpf.append(cpf)
            renda = float(input('digite a renda do cliente: '))
            if renda < 5000:
                lista_renda.append(renda)
                lista_a.append(cpf)
            elif renda >= 5000 and renda <= 10000:
                lista_renda.append(renda)
                lista_b.append(cpf)
            elif renda > 10000:
                lista_renda.append(renda)
                lista_c.append(cpf)
            novo = str(input('DESEJA CONTINUAR CADASTRANDO CLIENTES?(S/N)')).upper()
            if novo == 'N':
                print('-'*20)
                print('OPERAÇÃO REALIZADA COM SUCESSO!') 
                print('TOTAL DE CLIENTES CADASTRADOS :',len(lista_cpf))
                print('-'*30)
                print('FAIXA                              PORCENTAGEM')
                print('ABAIXO DE R$ 5000,00                  {:.2f}%'.format((len(lista_a)/len(lista_cpf))*100))
                print('ENTRE R$ 5000,00 E R$ 10000,00        {:.2f}%'.format((len(lista_b)/len(lista_cpf))*100))
                print('ACIMA DE R$ 10000,00                  {:.2f}%'.format((len(lista_c)/len(lista_cpf))*100))
                print('-'*30)
                retornar = int(input('APERTE 0 PARA RETORNAR A TELA PRINCIPAL'))
                if retornar == 0:
                    break
            elif novo == 'S':
                print('Proximo cliente')

            







