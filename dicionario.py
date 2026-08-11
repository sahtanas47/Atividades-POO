#questão 01

def contagem_caracteres(texto):
  contagm = {}

for letra in texto:
  if letra n contagem:
     contagem[letra] = contagem[letra] + 1
  else:
     contagem[letra = 1

return contagem


#questão 02

arquivo = open("estomago.txt", "r", encoding="utf-8")
texto = arquivo.read()
arquivo.close()

texto = texto.lower()
texto = texto.replace(".", " ")
texto = texto.replace(",", " ")
texto = texto.replace("!", " ")
texto = texto.replace("?", " ")
texto = texto.replace(";", " ")
texto = texto.replace(":", " ")

palavras = texto.split()
contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] = contagem[palavra] + 1
    else:
        contagem[palavra] = 1

ordenado = dict(sorted(contagem.items(), key=lambda item: item[1], reverse=True))

print(ordenado)


#questão 03

def mesclar_dicionarios(dicionario1, dicionario2):
    resultado = dicionario1.copy()

    for chave, valor in dicionario2.items():
        if chave in resultado:
            if valor > resultado[chave]:
                resultado[chave] = valor
        else:
            resultado[chave] = valor

    return resultado


#questão 04

def filtrar_dicionario(dicionario, chaves):
    resultado = {}

    for chave in chaves:
        if chave in dicionario:
            resultado[chave] = dicionario[chave]

    return resultado


#questão 05

def resultado_votacao(votos):
    totais = {}

    for votacao in votos:
        for candidato, quantidade in votacao.items():
            if candidato in totais:
                totais[candidato] = totais[candidato] + quantidade
            else:
                totais[candidato] = quantidade

    total_votos = sum(totais.values())
    resultado = {}

    for candidato, total in totais.items():
        percentual = (total / total_votos) * 100
        resultado[candidato] = (total, round(percentual, 2))

    return resultado
