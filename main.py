import matplotlib.pyplot as plt

print("Sistema de gerenciamento de livros")

print("Seja bem vindo! Escolha a opção desejada:")

livros = []

def cadastrar_livro():
    print("Cadastro de livro: ")
    titulo = input("Título: ")
    autor = input("Autor: ")
    while True:
        try:
            ano = int(input("Ano:"))
            break
        except ValueError:
            print("Resposta inválida. Por favor, digite um número para ano.")
    genero = input("Gênero: ")
    while True:
        try:
            quantidade = int(input("Quantidades disponíveis: "))
            break
        except ValueError:
            print("Resposta inválida. Por favor, digite um número para quantidade.")

    livros.append({"titulo": titulo, "autor": autor, "ano": ano, "genero": genero, "quantidades disponíveis": quantidade})
    print("Livro cadastrado com sucesso!")


def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        for i, livro in enumerate(livros, 1):
            print(f"{i}. Livro: {livro['titulo']} | Autor: {livro['autor']} | Ano: {livro['ano']} | Gênero: {livro['genero']} | Quantidades disponíveis: {livro['quantidades disponíveis']}")

    while True:
        termo = input("'voltar' para retornar ao menu:").lower()
        if termo == "voltar":
            break

def buscar_livro():
    while True:
        termo = input("Digite o título ou autor para buscar (ou 'voltar' para retornar ao menu): ").lower()
        if termo == "voltar":
            break

        encontrados = [l for l in livros if termo in l["titulo"].lower() or termo in l["autor"].lower()]

        if encontrados:
            print("Resultados encontrados:")
            for l in encontrados:
                print(f"{l['titulo']} - {l['autor']} | Quantidades: {l['quantidades disponíveis']}")
        else:
            print("Nenhum livro encontrado.")

def gerar_grafico():

    if not livros:
        print("Nenhum livro cadastrado para gerar o gráfico.")
        return

    genero = [l["genero"] for l in livros]
    quantidades = [l["quantidades disponíveis"] for l in livros]

    plt.bar(genero, quantidades, color='Royalblue')
    plt.title("Quantidade de livros por gênero")
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade")
    plt.yticks([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50])
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    termo = input("'voltar' para retornar ao menu:").lower()
    if termo == "voltar":
        return

while True:
    print("""
1 - Cadastrar um livro
2 - Lista de livros
3 - Buscar um livro
4 - Gerar gráfico de quantidades por gênero
5 - Sair""")
    opcao = input("Selecione a opção desejada: ")
    if opcao == "1":
        cadastrar_livro()
    elif opcao == "2":
        listar_livros()
    elif opcao == "3":
        buscar_livro()
    elif opcao == "4":
        gerar_grafico()
    elif opcao == "5":
        print("Você saiu.")
        break
    else:
        print("Opção inválida!")
