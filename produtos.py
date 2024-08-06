class Produto:
    def __init__(self,codproduto,nome,descricao,tamanho,preco):
        self.codproduto = codproduto
        self.nome = nome
        self.descricao = descricao
        self.tamanho = tamanho
        self.preco = preco

    def calcular(self):
        desconto = self.preco * 0.10
        preco_desconto = self.preco - desconto
        print(f'O preço com desconto do Produto {self.nome} é R${preco_desconto:.2f}')

produto1 = Produto('12813983','bottom', 'bottom exclusivo', '10cm', 2.99)
produto2 = Produto('1473747833','lapis', 'lapis fabber-castell', '15cm', 4.99)
produto3 = Produto('34773983','mochila', 'mochila da bagagio', '67cm', 129.50)

produto1.calcular()
produto2.calcular()
produto3.calcular()