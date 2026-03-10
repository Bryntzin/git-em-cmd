class Produtosele:
    def __init__(self, nome, marca,tipo, preco):
        self.nome = nome
        self.marca = marca
        self.tipo = tipo
        self.preco = preco
   
    def exibir(self):
        print(f"nome:{self.nome}, preço:{self.preco:.2f}, preco:{self.preco}")
 
class Tablet(Produtosele):
    def __init__(self, nome, marca, tipo, preco, memoria):
        super().__init__(nome, marca, tipo, preco)
        self.memoria = memoria
       
    def exibir(self):
        print(f"nome:{self.nome}, preço:{self.preco:.2f}, memoria:{self.memoria}")
 
 
class Smartfone(Produtosele):
    def __init__(self, nome, marca, tipo, preco, tamanho_tela):
        super().__init__(nome, marca, tipo, preco)
        self.tamanho_tela = tamanho_tela
       
    def exibir(self):
        print(f"nome:{self.nome}, preço:{self.preco:.2f}, tamanho_tela:{self.tamanho_tela}")
 
class Televisao (Produtosele):
    def __init__(self, nome, marca, tipo, preco, polegadas):
        super().__init__(nome, marca, tipo, preco)
        self.polegadas = polegadas
       
    def exibir(self):
        print(f"nome:{self.nome}, preço:{self.preco:.2f}, polegasdas:{self.polegadas}")
 
 