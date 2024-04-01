# Documentação do Projeto SisLoja

Este é um projeto de automação de processos de negócios para uma loja fictícia, denominado SisLoja. Na fase inicial, serão implantados os seguintes módulos do sistema SisLoja:

1) Gerenciamento de Estoque (GerEstoque)
2) Gerenciamento de Clientes (GerClientes)
3) Gerenciamento do Fluxo de Caixa (GerCaixa)

## Módulo GerEstoque

O módulo GerEstoque permite ao usuário incluir ou excluir itens no estoque da loja.

### Inclusão de Itens no Estoque:

- O usuário pode incluir vários itens ao estoque, informando quantos itens serão adicionados.
- Para cada item, o usuário deve fornecer o código do item (cod_item), uma descrição (desc_item) e seu valor em reais (valor_item).
- Após o cadastro dos itens, o sistema exibirá a média dos valores dos itens cadastrados e o código do item de maior valor com seu respectivo valor.

### Exclusão de Itens do Estoque:

- O usuário pode excluir itens do estoque digitando o código do item.
- Após digitar o código do item a ser excluído, o sistema emitirá uma mensagem de confirmação.
  - Se o usuário optar por não excluir o item, a operação será encerrada.
  - Se o usuário optar por excluir o item, o sistema verificará se o código é válido.
    - Se o código for inválido (soma dos dígitos inferior a 20), o sistema apresentará uma mensagem de erro e encerrará a operação.
    - Se o código for válido e houver saldo em estoque, o item será excluído e o sistema apresentará uma mensagem de sucesso.
- Após a exclusão de todos os itens, o sistema apresentará uma lista dos itens excluídos e o saldo restante em estoque.

## Módulo GerClientes

O módulo GerClientes permite cadastrar clientes da loja, utilizando o CPF e a renda do cliente.

- O usuário pode cadastrar vários clientes digitando o CPF e a renda do cliente.
- A operação pode ser interrompida quando o usuário digitar um CPF igual a 0.
- O sistema verifica se o CPF do cliente é válido.
- Após o cadastro dos clientes, o sistema exibe uma mensagem de sucesso, seguida do número de clientes cadastrados e do percentual de clientes com renda superior a R$ 10.000,00, entre R$ 5.000,00 e R$ 10.000,00, e inferior a R$ 5.000,00.

## Módulo GerCaixa

O módulo GerCaixa permite ao usuário registrar a movimentação financeira diária da loja.

- O usuário insere a data, o saldo inicial do caixa e o número total de vendas realizadas.
- Em seguida, o usuário registra as vendas de cada cliente, especificando o CPF do cliente e o número de compras realizadas.
- Para cada compra, o usuário registra o código do item, a quantidade de itens e o valor unitário.
- O sistema calcula o valor total da venda para cada cliente.
- O sistema exibe um relatório parcial com o valor total das vendas por cliente.
- Após o registro de todas as vendas, o sistema apresenta um relatório com a data da movimentação, o saldo final do caixa, o valor médio das vendas, o total de itens vendidos e o código do cliente que mais consumiu.

## Desenvolvimento

Este projeto foi desenvolvido como parte do curso na faculdade.

---
Espero que esta documentação seja útil para o seu projeto! Se precisar de mais alguma coisa, não hesite em perguntar.

