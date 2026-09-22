class Animal:
    def __init__(self, nome, idade, nivel_fome):
        self.__nome = nome
        self.idade = idade
        self.nivel_fome = nivel_fome

    # Getter e setter do nome
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    # Getter e setter da idade
    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, valor):
        if valor < 0:
            print("Erro: Idade inválida")
        else:
            self.__idade = valor

    # Getter e setter do nível de fome
    @property
    def nivel_fome(self):
        return self.__nivel_fome

    @nivel_fome.setter
    def nivel_fome(self, valor):
        if valor < 0:
            self.__nivel_fome = 0
        elif valor > 100:
            self.__nivel_fome = 100
        else:
            self.__nivel_fome = valor

    # Alimenta o animal
    def alimentar(self, porcao):
        if porcao <= 0:
            print("Erro: Porção inválida")
        else:
            self.nivel_fome = self.nivel_fome - porcao

    # Som genérico
    def emitir_som(self):
        print(f"{self.nome} faz um som genérico.")

    # Resumo do animal
    def exibir_resumo(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Nível de fome: {self.nivel_fome}")


class Mamifero(Animal):
    def __init__(self, nome, idade, nivel_fome, velocidade_kmh):
        super().__init__(nome, idade, nivel_fome)
        self.__velocidade_kmh = velocidade_kmh

    # Getter e setter da velocidade
    @property
    def velocidade_kmh(self):
        return self.__velocidade_kmh

    @velocidade_kmh.setter
    def velocidade_kmh(self, valor):
        self.__velocidade_kmh = valor

    # Correr aumenta a fome
    def correr(self):
        self.nivel_fome = self.nivel_fome + 20
        print(f"{self.nome} correu a {self.velocidade_kmh} km/h!")

    # Sobrescrita do método da classe Animal
    def emitir_som(self):
        print(f"{self.nome} ruge/ruge alto!")

    # Sobrescrita do resumo
    def exibir_resumo(self):
        super().exibir_resumo()
        print(f"Velocidade de corrida: {self.velocidade_kmh} km/h")


class Ave(Animal):
    def __init__(self, nome, idade, nivel_fome, envergadura_asas):
        super().__init__(nome, idade, nivel_fome)
        self.__envergadura_asas = envergadura_asas

    # Getter e setter da envergadura
    @property
    def envergadura_asas(self):
        return self.__envergadura_asas

    @envergadura_asas.setter
    def envergadura_asas(self, valor):
        self.__envergadura_asas = valor

    # Voar depende do nível de fome
    def voar(self):
        if self.nivel_fome > 80:
            print(
                f"Voo negado: {self.nome} está faminto demais para voar!"
            )
        else:
            print(
                f"{self.nome} voou com suas asas de "
                f"{self.envergadura_asas}cm!"
            )
            self.nivel_fome = self.nivel_fome + 15

    # Sobrescrita do método da classe Animal
    def emitir_som(self):
        print(f"{self.nome} canta um som melodioso!")

    # Sobrescrita do resumo
    def exibir_resumo(self):
        super().exibir_resumo()
        print(f"Envergadura das asas: {self.envergadura_asas} cm")

# TESTES OBRIGATÓRIOS

# Instanciando os animais
leao = Mamifero(
    nome="Simba",
    idade=5,
    nivel_fome=70,
    velocidade_kmh=80
)

gaviao = Ave(
    nome="Sky",
    idade=2,
    nivel_fome=75,
    envergadura_asas=120
)

# 1. Tentativa de alteração direta dos atributos privados
leao.__nivel_fome = -999
leao.__idade = -10

# Os atributos reais não foram alterados.
# O Python cria atributos diferentes por causa do name mangling.

# 2. Testando ações que alteram o estado interno
leao.correr()          # Fome: 70 -> 90
gaviao.voar()          # Fome: 75 -> 90
gaviao.voar()          # Voo negado, pois fome = 90

# 3. Testando alimentação
leao.alimentar(50)     # Fome: 90 -> 40
leao.alimentar(-10)    # Erro

# 4. Exibição final dos resumos
print("\n--- RESUMO DO MAMÍFERO ---")
leao.emitir_som()
leao.exibir_resumo()

print("\n--- RESUMO DA AVE ---")
gaviao.emitir_som()
gaviao.exibir_resumo()
