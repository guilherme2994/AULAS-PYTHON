# QUESTÃO 2 - VALIDAÇÃO DE SENHA

senha_correta = "123456"

senha = input("Digite a senha: ")

while senha != senha_correta:
    print("Senha incorreta. Tente novamente.")
    senha = input("Digite a senha: ")

print("Acesso permitido!")
