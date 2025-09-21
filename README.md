# Controle de Consumo de Insumos


## Descrição do Projeto
Este projeto implementa um sistema de controle de consumo de insumos, permitindo:  
- Adicionar itens consumidos com quantidade e validade;  
- Visualizar o consumo em ordem de inserção (fila) ou inversa (pilha);  
- Buscar itens utilizando busca sequencial ou binária;  
- Ordenar itens por quantidade ou por validade;  
- Gerar relatórios em Markdown com todos os registros.  

O sistema é desenvolvido em **Python**, utilizando a estrutura de dados `deque` para simular a fila e pilha, a biblioteca `datetime` para registrar datas, e funções auxiliares para organizar, buscar e ordenar os dados.

## Estruturas de Dados
- **Fila (`deque`)**: mantém os itens na ordem em que foram adicionados, permitindo visualização sequencial ou inversa.  
- **Tuplas**: cada item é armazenado como uma tupla contendo: nome, quantidade, data de registro e validade.  

## Funcionalidades

### Adicionar Item
Permite inserir um novo item no sistema com:  
- Nome do item;  
- Quantidade;  
- Validade do produto;  
- Data e hora do registro (automaticamente registrada).  

### Visualizar Consumo
- **Ordem de inserção (fila)**: mostra os itens na ordem em que foram adicionados.  
- **Ordem inversa (pilha)**: exibe os itens do último adicionado para o primeiro.

### Buscar Item
- **Busca Sequencial**: percorre todos os itens até encontrar o que corresponde ao nome informado.  
- **Busca Binária**: exige que a lista esteja ordenada pelo nome; permite encontrar itens de forma mais rápida comparando elementos pela metade da lista repetidamente.

### Ordenar Itens
- **Por Quantidade**: organiza os itens do menor para o maior número de unidades.  
- **Por Validade**: organiza os itens pela data de validade mais próxima, convertendo a string da validade para data para garantir a ordem correta.

### Gerar Relatório
Gera um arquivo em Markdown (`relatorio.md`) contendo todos os itens cadastrados, com:  
- Nome do item;  
- Quantidade;  
- Data de registro;  
- Validade (quando informada).  

O relatório pode ser utilizado para documentação ou impressão.

## Menu Principal
O sistema possui um menu interativo com as seguintes opções:  
1. Adicionar consumo  
2. Ver consumo do dia (fila)  
3. Ver consumo invertido (pilha)  
4. Buscar item (sequencial ou binária)  
5. Ordenar por quantidade  
6. Gerar relatório  
7. Ordenar por validade  
0. Sair  

Cada opção aciona a funcionalidade correspondente, permitindo controle completo dos insumos.

## Observações
- A fila (`deque`) garante a ordem de entrada, enquanto o inverso simula a pilha.  
- A busca binária exige que a lista esteja ordenada, mas é mais eficiente para listas grandes.  
- A validade dos produtos é considerada para ordenação e visualização.  
- Relatórios são gerados automaticamente em Markdown para facilitar documentação ou compartilhamento.  

## Tecnologias Utilizadas
- **Python 3**  
- **Deque (`collections`)**  
- **Datetime (`datetime`)**  
- **Funções auxiliares para organização, busca e ordenação**  


## Integrantes
- **Marcela Torro** - 557658  
- **Gustavo** - 559098  
- **Matheus A.** - 555177  
- **Rodrigo** - 550266  
