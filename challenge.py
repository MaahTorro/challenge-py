# Integrantes: 
# Marcela Torro - 557658
# Gustavo - 559098
# Matheus - 555177
# Rodrigo - 550266


from collections import deque
from datetime import datetime


def print_titulo(texto):
    print(f"\n\033[1;36m{'=' * 50}\033[0m")
    print(f"\033[1;36m{texto.center(50)}\033[0m")
    print(f"\033[1;36m{'=' * 50}\033[0m")

def print_divisor():
    print("\n\033[1;90m" + "-" * 50 + "\033[0m\n")

def print_lista(lista):
    if not lista:
        print("⚠️ Nenhum item registrado ainda.")
        return
    for i, item in enumerate(lista, 1):
        if len(item) == 4:
            nome, qtd, data, validade = item
            print(f"{i}. [{data}] {nome} → {qtd} unidades (Validade: {validade})")
        else:
            nome, qtd, data = item
            print(f"{i}. [{data}] {nome} → {qtd} unidades")

fila_consumo = deque()

def adicionar_item():
    print_divisor()
    nome = input("Digite o nome do item: ").strip()
    qtd = int(input("Digite a quantidade: "))
    validade = input("Digite a validade do produto (dd/mm/aaaa): ").strip()
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    fila_consumo.append((nome, qtd, data, validade))
    print("✅ Item adicionado com sucesso!")

def mostrar_fila():
    print_divisor()
    print_titulo("CONSUMO EM ORDEM (FILA)")
    print_lista(list(fila_consumo))

def mostrar_pilha():
    print_divisor()
    print_titulo("CONSUMO EM ORDEM INVERSA (PILHA)")
    pilha = list(fila_consumo)[::-1]
    print_lista(pilha)

def busca_sequencial(lista, nome_item):
    for i, item in enumerate(lista):
        nome = item[0]
        if nome.lower() == nome_item.lower():
            return i, item
    return None

def busca_binaria(lista, nome_item):
    lista_ordenada = sorted(lista, key=lambda x: x[0].lower())
    inicio, fim = 0, len(lista_ordenada) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        nome = lista_ordenada[meio][0]
        if nome.lower() == nome_item.lower():
            return meio, lista_ordenada[meio]
        elif nome_item.lower() < nome.lower():
            fim = meio - 1
        else:
            inicio = meio + 1
    return None

def buscar_item():
    print_divisor()
    if not fila_consumo:
        print("⚠️ Nenhum item registrado.")
        return

    nome_item = input("Digite o nome do item para buscar: ").strip()
    print("Escolha o tipo de busca:")
    print("1 - Sequencial")
    print("2 - Binária (precisa de lista ordenada)")
    opcao = input("> ")

    if opcao == "1":
        resultado = busca_sequencial(fila_consumo, nome_item)
    else:
        resultado = busca_binaria(fila_consumo, nome_item)

    if resultado:
        i, item = resultado
        if len(item) == 4:
            nome, qtd, data, validade = item
            print(f"🔎 Encontrado: [{data}] {nome} → {qtd} unidades (Validade: {validade})")
        else:
            nome, qtd, data = item
            print(f"🔎 Encontrado: [{data}] {nome} → {qtd} unidades")
    else:
        print("❌ Item não encontrado.")

def ordenar_por_quantidade():
    print_divisor()
    if not fila_consumo:
        print("⚠️ Nenhum item registrado.")
        return
    lista = sorted(fila_consumo, key=lambda x: x[1])
    print_titulo("ORDENADO POR QUANTIDADE")
    print_lista(lista)

def ordenar_por_validade():
    print_divisor()
    if not fila_consumo:
        print("⚠️ Nenhum item registrado.")
        return
    
    def parse_validade(item):
        try:
            return datetime.strptime(item[3], "%d/%m/%Y")
        except:
            return datetime.max  
    
    lista = sorted(fila_consumo, key=parse_validade)
    print_titulo("ORDENADO POR VALIDADE")
    print_lista(lista)

def gerar_relatorio():
    print_divisor()
    if not fila_consumo:
        print("⚠️ Nenhum item registrado.")
        return
    with open("relatorio.md", "w", encoding="utf-8") as f:
        f.write("# Relatório de Consumo\n\n")
        for item in fila_consumo:
            if len(item) == 4:
                nome, qtd, data, validade = item
                f.write(f"- [{data}] {nome}: {qtd} unidades (Validade: {validade})\n")
            else:
                nome, qtd, data = item
                f.write(f"- [{data}] {nome}: {qtd} unidades\n")
    print("📄 Relatório salvo como 'relatorio.md'")


while True:
    print_titulo("MENU PRINCIPAL")
    print("1. ➕ Adicionar consumo")
    print("2. 📜 Ver consumo do dia")
    print("3. 🔄 Ver consumo invertido")
    print("4. 🔎 Buscar item")
    print("5. 📊 Ordenar por quantidade")
    print("6. 📝 Gerar relatório")
    print("7. 📅 Ordenar por validade")
    print("0. ❌ Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_item()
    elif opcao == "2":
        mostrar_fila()
    elif opcao == "3":
        mostrar_pilha()
    elif opcao == "4":
        buscar_item()
    elif opcao == "5":
        ordenar_por_quantidade()
    elif opcao == "6":
        gerar_relatorio()
    elif opcao == "7":
        ordenar_por_validade()
    elif opcao == "0":
        print_divisor()
        print("Saindo...")
        break
    else:
        print_divisor()
        print("⚠️ Opção inválida. Tente novamente.")

        

