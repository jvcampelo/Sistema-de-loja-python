# GerCaixa


# dar um import da lista de cpfs (código dos clientes) do GerCliente
import GerClientes
import GerStoque

lista_clientes = GerClientes.lista_cpf  # pegar no GerCliente
total_gasto_cliente = []
total_qtd_produtos_vendidos = []


lista_valores_produtos = GerStoque.preco_item # pegar no GerEstoque
lista_cod_item = GerStoque.codigos # pegar no GerEstoque

def lancamento_dados():
    data = input('Qual é a data do dia? [dd/mm/aaaa]: ') # pesquisar como verificar
    saldo_inicial = input('Saldo inicial do dia: ')
    num_total_vendas_realizadas = int(input('Número total de vendas realizadas no dia: '))
    for cpf in lista_clientes:
        qtd_compras = int(input(f'Quantos tipos de produtos o cliente com o {cpf} comprou? '))
        i = 1
        soma_compras = 0
        soma_qtd_itens = 0
        while i <= qtd_compras:
            while True:
                cod_item = int(input(f'Qual é o código do {i}° item? '))
                if cod_item not in lista_cod_item:
                    print('O item que você digitou não esta em nosso sistema, tente novamente ')
                    cod_item = int(input(f'Qual é o código do {i}° item? '))

                else:
                    break
            while True:
                quant_item = input('Quantas unidades desse item? ')
                try:
                    quant_item = int(quant_item)
                    break
                except:
                    print('Valor inválido. É preciso inserir um número. Tente novamente: ')
            index = lista_cod_item.index(cod_item)
            valor_item = lista_valores_produtos[index]
            valor_compra = quant_item * valor_item
            soma_compras = soma_compras + valor_compra
            soma_qtd_itens = soma_qtd_itens + quant_item
            i += 1
        total_gasto_cliente.append(soma_compras)
        total_qtd_produtos_vendidos.append(soma_qtd_itens)
    relatorio_por_cliente(lista_clientes)
    relatorio(data, saldo_inicial, num_total_vendas_realizadas)

def relatorio_por_cliente(lista_clientes):
    print('-' * 50)
    for cpf in lista_clientes:
        print(f'Cliente {cpf} Total de vendas: R$ {total_gasto_cliente[lista_clientes.index(cpf)]}')
    print('-' * 50)

def relatorio(data, saldo_inicial, num_total_vendas_realizadas):
    valor_medio_vendas = sum(total_gasto_cliente) / num_total_vendas_realizadas
    cliente_maior_consumo = lista_clientes[total_gasto_cliente.index(max(total_gasto_cliente))]
    print('-' * 50)
    print('RELATÓRIO DE VENDAS')
    print(f'Data da movimentação: {data}')
    print(f'Saldo : R$ {saldo_inicial}')
    print(f'Valor médio das vendas: R$ {valor_medio_vendas}')
    print(f'Total das vendas: R$ {sum(total_qtd_produtos_vendidos)} unidades')
    print(f'Cliente de maior consumo: Código {cliente_maior_consumo}')
    print('-' * 50)


def Gercaixa():
  lancamento_dados()
  
