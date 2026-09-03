#Atividade 2 - Operadores

#Crie um algoritmo, que faça um formulário em que o usuário DIGITE seu nome, sua idade e se ele tem plano de saúde (True ou False)
#O eu sistema deve retornar em um único print(), todas as informações, e se ele for menor de idade ou idoso ou se não tiver plano de saúde, que ele não será aceito no nosso formulário;
#Exemplo de retorno no terminal: Seu nome é João, você tem 22 anos.
#Tem plano? False. Você foi aceito? False.


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
plano = input("Você tem plano de saúde? (True ou False): ")

# Converte o texto digitado para booleano
plano = plano == "True"

aceito = idade >= 18 and idade < 60 and plano == True

print(f"Seu nome é {nome}, você tem {idade} anos. Tem plano? {plano}. Você foi aceito? {aceito}.")
