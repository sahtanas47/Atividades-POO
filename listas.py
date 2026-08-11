#questao 01

lista = []

quantidade = int(input("Quantos números voce quer digitar?"))

while quantidade < 4:
  print("Digite pelo menos 4 números.")
  quantidade = int(input("Quantos números voce quer digitar?."))

for i in range(quantidade):
  numero = int(input("Digite um número:"))
  lista.append(numero)

print("Lista original:", lista)
print("3 primeiros:", lista[:3])
print("2 últimos:", lista[-2:])
print("Lista invertida:", lista[::-1])
print("Índices pares:", lista[0::2])
print("Índices ímpares:", lista[1::2])



#questão 02

urls = [
  "www.google.com",
  "www.gmail.com",
  "www.github.com",
  "www.reddit.com",
  "www.yahoo.com"
]

dominios = []

for url in urls:
  nome = url[4:-4]
  dominios.append(nome)
print("URLs:", urls)
print("Dominios:", dominios)



#questão 03

from random import randint

lista = []

for i in range(10):
  numero = randint(-100, 100)
  lista.append(numero)

ordenada = sorted(lista)

print("Lista ordenada:", ordenada)
print("Lista original:", lista)

print("Índice do maior valor:", lista.index(max(lista)))
print("Índice do menor valor:", lista.index(min(lista)))

soma = sum(lista)
media = soma / len(lista)

print("Soma:", soma)
print("Média:", media)



#questão 04

lista1 = []
lista2 = []
lista3 = []

qtd1 = int(input("Digite a quantidade de elementos da lista 1: "))

print("Digite os elementos da lista 1:" )
for i in range(qtd1):
  numero = int(input())
  lista1.append(numero)

qtd2 = int(input("Digite a quantidade de elementos da lista 2: "))

print("Digite os elementos da lista 2:")
for i in range(qt21):
  numero = int(input())
  lista2.append(numero)

menor = min(len(lista1), len(lista2))

for i in range(menor):
  lista3.append(lista1[i])
  lista3.append(lista2[i])

if len(lista1) > len(lista2):
  for i in range(menor, len(lista1)):
    lista3.append(lista1[i])

else:
  for i in range(menor, len(lista2)):
    lista3.append(lista2[i])

    print("Lista intercalada:", lista3)



#questão 05

from random import randint

lista1 = []
lista2 = []
interseccao = []

for i in range(20):
  lista1.append(randint(0, 50))
  lista2.append(randint(0, 50))

for numero in lista1:
  if numero in lista2 and numero not in interseccao:
    interseccao.append(numero)

interseccao.sort()

print("Lista 1:", lista1)
print("Lista2:", lista2)
print("Interseccao", interseccao)



#questão 06

from random import randint

lista = []

for i in range(20):
  lista.append(randint(0, 100))

print("Lista original:", lista)

tamanho = int(input("Digite o tamanho das partes: "))

sublistas = []

for i in range(0, len(lista), tamanho):
  parte = lista[i:i + tamanho]
  sublistas.append(parte)

print("Sublistas:", sublistas)


#questão 07

n = int(input("Digite o tamanho da matriz: "))

matriz = []

for i in range(n):
    linha = []

    for j in range(n):
        linha.append(i)

    matriz.append(linha)

print(matriz)




        
