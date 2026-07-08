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

#questao05
# Questão 5

frase = input("Digite uma frase: ")

total = 0

print("Índices das vogais:")

for i in range(len(frase)):
    if frase[i].lower() in "aeiou":
        print(i, end=" ")
        total = total + 1

print()
print("Total:", total, "vogais")

#questao06

lista = []

quantidade = int(input("Quantos números deseja digitar? (mínimo 4): "))

while quantidade < 4:
    quantidade = int(input("Digite pelo menos 4 números: "))

for i in range(quantidade):
    numero = int(input("Digite um número: "))
    lista.append(numero)

print("Lista original:", lista)
print("3 primeiros:", lista[:3])
print("2 últimos:", lista[-2:])
print("Lista invertida:", lista[::-1])
print("Índices pares:", lista[::2])
print("Índices ímpares:", lista[1::2])

#questao07

urls = [
    "www.google.com",
    "www.gmail.com",
    "www.github.com",
    "www.reddit.com",
    "www.yahoo.com"
]

dominios = []

for site in urls:
    dominios.append(site[4:-4])

print("URLs:", urls)
print("Domínios:", dominios)

# Questão08

from random import randint

lista = []

for i in range(10):
    lista.append(randint(-100, 100))

ordenada = sorted(lista)

print("Lista ordenada:", ordenada)
print("Lista original:", lista)

maior = max(lista)
menor = min(lista)

print("Índice do maior:", lista.index(maior))
print("Índice do menor:", lista.index(menor))

print("Soma:", sum(lista))
print("Média:", sum(lista) / len(lista))

# Questão09

lista1 = []
lista2 = []
lista3 = []

qtd1 = int(input("Quantidade da lista 1: "))

for i in range(qtd1):
    numero = int(input("Digite um número: "))
    lista1.append(numero)

qtd2 = int(input("Quantidade da lista 2: "))

for i in range(qtd2):
    numero = int(input("Digite um número: "))
    lista2.append(numero)

menor = qtd1

if qtd2 < qtd1:
    menor = qtd2

for i in range(menor):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

if qtd1 > qtd2:
    for i in range(menor, qtd1):
        lista3.append(lista1[i])

else:
    for i in range(menor, qtd2):
        lista3.append(lista2[i])

print("Lista intercalada:", lista3)

# Questão09

from random import randint

lista1 = []
lista2 = []
interseccao = []

for i in range(20):
    lista1.append(randint(0, 50))

for i in range(20):
    lista2.append(randint(0, 50))

for numero in lista1:
    if numero in lista2:
        if numero not in interseccao:
            interseccao.append(numero)

interseccao.sort()

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseção:", interseccao)

# Questão10

from random import randint

lista = []

for i in range(20):
    lista.append(randint(0, 100))

print("Lista:", lista)

tamanho = int(input("Tamanho das sublistas: "))

sublistas = []

for i in range(0, len(lista), tamanho):
    sublistas.append(lista[i:i+tamanho])

print(sublistas)

# Questão11

n = int(input("Digite n: "))

matriz = []

for i in range(n):

    linha = []

    for j in range(n):
        linha.append(i)

    matriz.append(linha)

print(matriz)


