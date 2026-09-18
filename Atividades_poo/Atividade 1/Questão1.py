# Crie uma classe que tenha no mínimo 5 atributos, 1 construtor, 3 métodos convencionais.

# Sua classe deve ser uma das opções abaixo:
#     Carro
#     Banco
#     Pessoa

# Você escolhe quais atributos relacionar com o conceito da sua classe.

# No final, quero 5 objetos diferentes instanciados, e seu programa deve exibir em uma lista FORA da classe todos os seus objetos.

class Carro:
    def __init__(self, marca, modelo, ano, cor, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 20

    def frear(self):
        self.velocidade = max(0, self.velocidade - 20)

    def mostrar_informacoes(self):
        return f"{self.marca} {self.modelo} - {self.ano} - {self.cor} - {self.velocidade} km/h"


# 5 objetos diferentes
carro1 = Carro("Toyota", "Corolla", 2022, "Prata", 80)
carro2 = Carro("Honda", "Civic", 2023, "Preto", 60)
carro3 = Carro("Volkswagen", "Golf", 2021, "Azul", 90)
carro4 = Carro("Chevrolet", "Onix", 2024, "Branco", 50)
carro5 = Carro("Ford", "Mustang", 2020, "Vermelho", 100)

# Lista FORA da classe contendo todos os objetos
carros = [carro1, carro2, carro3, carro4, carro5]

# Exibindo todos os objetos
for carro in carros:
    print(carro.mostrar_informacoes())
