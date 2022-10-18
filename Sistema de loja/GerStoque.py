codigos = list()
Qtd_itens = list()
descrição_item = list()
preco_item = list()
codigos_apagados = list()
saldos_apagados = list()
#funçao pra somar os digitos de um numero
def soma_codigo(codigo):
    String = str(codigo) 
    lista_de_numero = list(map(int, String.strip())) 
    return sum(lista_de_numero)
# funçao para calcular a media dos elementos de uma lista
def media():
    return sum(preco_item)/len(preco_item)
#funçao pra definir o codigo do item com o maior preço
def Maior_preço( ):
    indexPreço = preco_item.index(max(preco_item))
    indexCodigo= indexPreço
    print('o codigo do item de maior valor cadastrado é {} e seu preço é {}R$'.format(codigos[indexCodigo],preco_item[indexPreço]))
#funçao pra relacionar iten excluido com seu preço para poder excluir eles da lista 
def apagar_item(codigo):
    if codigo in  codigos:
            index = codigos.index(codigo)
            del codigos[index]
            qtd = Qtd_itens[index]
            del Qtd_itens[index]
            del preco_item[index]
            codigos_apagados.append(codigo)
            saldos_apagados.append(qtd)
           
    else:
            print('Esse codigo Não esta na lista') 
#função pra montar a tabela de itens apagados do sitema
def tabela_apagados():
    a = 0
    print('-'*30)
    print('RELATÓRIO DE ITENS EXCLUÍDOS')
    print('ITEM\t\tSALDO')
    for c in range(len(codigos_apagados)):
        print('%.d\t\t%.d'%(codigos_apagados[a], saldos_apagados[a]))
        a = a+1
    print('-'*30)
#função para o usuario incluir itens ao estoque
def incluir():
    
    while True:
        codigo = int(input('digite o codigo do produto:'))
        if soma_codigo(codigo)<=20:
            print('Digite novamente')
        else:
            codigos.append(codigo)
            qtd = int(input('qual é a quantidade de itens:'))
            Qtd_itens.append(qtd)
            preço = str(input('qual é o preço do item?'))
            preço = preço.split()[0]
            preço = int(preço)
            preco_item.append(preço)
            descrição = str(input('digite a descrição do item:'))
            descrição_item.append(descrição)
            pergunta = str(input('deseja continuar incluindo itens?(S/N)')).upper()
            if pergunta == 'N':
                print('-'*30)
                print('O valor médio dos itens cadastrados é {:.2f} R$'.format(media()))
                Maior_preço()
                print('-'*30)
                break
            elif pergunta == 'S':
                print('Proximo item...')
#função para excluir itens do estoque
def excluir():         
    
    while True:
        codigo = int(input('Digite o codigo do item que você deseja excluir:'))
        if codigo not in codigos:
            print('codigo invalido')
            print('digite novamente')
        else:
            pergunta = str(input('Tem certeza que desea exlcuir o item?(S/N)').upper())
            if pergunta == 'N':
                print('O item não foi excluido') 
            else:
                apagar_item(codigo)
                print('ITEM EXCLUIDO')
                continuar = str(input('deseja contiuar ecluindo itens?(S/N)').upper())
                if continuar == 'N':
                    tabela_apagados()
                    
                    break

def Gerstoque():
    while True: 
        pergunta = str(input('Você deseja incluir ou excluir itens? ').upper())
        if pergunta == 'INCLUIR':
            incluir()
            tela_principal = int(input('digite 0 para voltar a tela principal: '))
            if tela_principal == 0:
                break
        elif pergunta == 'EXCLUIR':
            excluir()
            tela_principal = int(input('digite 0 para voltar a tela principal: '))
            if tela_principal == 0:
                break


                 
                     

            
         
          
            
            
    

            
        
            
           






    
   
