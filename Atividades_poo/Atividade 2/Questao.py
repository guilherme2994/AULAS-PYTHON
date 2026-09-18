class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.__quantidade_estoque += quantidade
        else:
            print("Erro: Quantidade inválida")

    def realizar_venda(self, quantidade):
        if quantidade > 0 and quantidade <= self.__quantidade_estoque:
            self.__quantidade_estoque -= quantidade
            print("Venda realizada com sucesso")
        elif quantidade > self.__quantidade_estoque:
            print("Venda negada: Estoque insuficiente")
        else:
            print("Erro: Quantidade inválida")

    def aplicar_desconto(self, percentual):
        if percentual > 0 and percentual <= 80:
            desconto = self.__preco * (percentual / 100)
            self.__preco -= desconto
        else:
            print("Erro: Desconto inválido")

    def exibir_resumo(self):
        print("Nome:", self.__nome)
        print("Preço:", self.__preco)
        print("Quantidade em estoque:", self.__quantidade_estoque)


# Criação do produto de teste
meu_produto = Produto("Notebook", 3000.00, 10)

# 1. Tentativa de alteração direta dos atributos
meu_produto.__quantidade_estoque = -50
meu_produto.__preco = -100

# 2. Tentativa de realizar uma venda maior que o estoque
meu_produto.realizar_venda(9999)

# 3. Exibição do resumo final
meu_produto.exibir_resumo()

# Exibe os dados reais armazenados no objeto
print("\nDados internos do objeto:")
print(meu_produto.__dict__)
