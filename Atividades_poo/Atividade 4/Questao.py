from abc import ABC, abstractmethod

# 1. CLASSE PAI ABSTRATA (Contrato do Sistema)

class Transportadora(ABC):
    """Classe Pai Abstrata que define o contrato obrigatório para o cálculo de frete."""

    def registrar_log(self, nome_servico: str) -> None:
        """Método concreto: Comum a todas as filhas, possui corpo e realiza log no sistema central."""
        print(
            f"[LOG SISTEMA CENTRAL] Iniciando processamento de frete via: {nome_servico}"
        )

    @abstractmethod
    def calcular_frete(self, distancia_km: float, peso_kg: float) -> float:
        """Método abstrato: Define a assinatura obrigatória que todas as filhas devem implementar."""
        pass


# 2. CLASSES FILHAS (Implementações Concretas)

class Caminhao(Transportadora):
    """Classe filha para transporte terrestre rodoviário."""

    def calcular_frete(self, distancia_km: float, peso_kg: float) -> float:
        self.registrar_log("Caminhão")
        # Regra de negócio: R$ 5,00 por Km rodado
        valor_total = distancia_km * 5.00
        print(
            f"   -> Caminhão | Distância: {distancia_km} km | Custo: R$ {valor_total:.2f}"
        )
        return valor_total


class Drone(Transportadora):
    """Classe filha para transporte aéreo leve com restrição de peso."""

    def calcular_frete(self, distancia_km: float, peso_kg: float) -> float:
        self.registrar_log("Drone")
        # Validação específica: Drone só suporta cargas de até 2.0 kg
        if peso_kg > 2.0:
            print(
                f"   -> Drone FALHOU: Carga de {peso_kg} kg excede o limite máximo de 2.0 kg."
            )
            return 0.0

        # Regra de negócio: R$ 20,00 por Km rodado
        valor_total = distancia_km * 20.00
        print(
            f"   -> Drone | Distância: {distancia_km} km | Peso: {peso_kg} kg | Custo: R$ {valor_total:.2f}"
        )
        return valor_total


class Navio(Transportadora):
    """Classe filha para transporte marítimo com taxa portuária fixa."""

    def calcular_frete(self, distancia_km: float, peso_kg: float) -> float:
        self.registrar_log("Navio")
        # Regra de negócio: R$ 2,00 por Km + Taxa portuária fixa de R$ 100,00
        taxa_portuaria = 100.00
        valor_total = (distancia_km * 2.00) + taxa_portuaria
        print(
            f"   -> Navio | Distância: {distancia_km} km | Custo (com taxa portuária): R$ {valor_total:.2f}"
        )
        return valor_total


# 3. O SISTEMA (Função Polimórfica Externa)

def processar_lote(
    lista_de_objetos: list, distancia_km: float, peso_kg: float
) -> None:
    """Recebe um lote de transportadoras e executa as operações de forma polimórfica."""
    print("\n--- INICIANDO PROCESSAMENTO EM LOTE ---")
    for item in lista_de_objetos:
        # A função não precisa saber qual é a classe concreta exata;
        # ela apenas confia no contrato da interface 'Transportadora'.
        item.calcular_frete(distancia_km, peso_kg)
        print("-" * 50)


# ROTEIRO DE TESTES

if __name__ == "__main__":

    # 1. Tentativa de instanciar a Classe Abstrata (DEVE GERAR ERRO)
    # Descomente a linha abaixo para testar e provar que o Python bloqueia a instanciação:
    # objeto_generico = Transportadora()  # TypeError: Can't instantiate abstract class Transportadora with abstract method calcular_frete

    # 2. Instanciando as Classes Filhas
    caminhao = Caminhao()
    drone = Drone()
    navio = Navio()

    # 3. Criando um Lote de Processamento (Lista de Objetos)
    lote = [caminhao, drone, navio, caminhao]

    # 4. Processando em lote (Demonstrando o Polimorfismo e a Abstração)

    # Cenario A: Carga leve (1.5 kg, 50 km) - O Drone aceita o envio
    print("=== CENÁRIO A: Carga de 1.5 kg para 50 km ===")
    processar_lote(lote, distancia_km=50, peso_kg=1.5)

    # Cenario B: Carga pesada (5.0 kg, 50 km) - O Drone rejeita por ultrapassar 2 kg
    print("=== CENÁRIO B: Carga de 5.0 kg para 50 km ===")
    processar_lote(lote, distancia_km=50, peso_kg=5.0)