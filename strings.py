#questao01
primeiro_nome = (input("Digite seu primeiro nome: "))
segundo_nome = (input("Digite seu segumdo nome: "))

print(f"Bem vinda(o), {primeiro_nome} {segundo_nome}!")

#questao02
frase = "Eu gosto muito de programar!"
quantidade = frase.count(" ")
print(quantidade)

#questao03
nome = input("Digite o seu nome: ").upper()

for i in range(1, len(nome) + 1):
    print(nome[:i])
#questao04
numero = (input("Digite seu número de telefone:"))
if len(numero) == 8:
    numero = "9" + numero
elif len(numero) == 9:
    if numero[0] != "9":
        print("Seu número é inválido! Deve conter o número 9 na frente.")

        exit()

formatacao = numero[:5] + "-" + numero[5:]


print("Número completo:", formatacao)
