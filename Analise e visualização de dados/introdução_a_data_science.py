# -*- coding: utf-8 -*-
"""Introdução a Data Science.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11X0RTmmH4BySiBfCuBDK_uwwgo_0zgIU
"""

import pandas as pd #Importando a biblioteca pandas

notas = pd.read_csv("ratings.csv") #Lendo o arquivo csv

notas.head() #5 primeiros elementos

notas.shape[0] #Quantidade de linhas

notas.columns = ["usuarioId", "filmeId", "notas", "momento"] #Trocando o nome das colunas
notas.head()

notas["notas"] #Uma serie

notas["notas"].unique() #Achar os valores presentes na coluna

notas["notas"].value_counts() #Contar quantidade de vezes que cada elemento apareceu na coluna

print("Media:" ,notas["notas"].mean()) #Média de todas as notas
print("Mediana:" ,notas.notas.median()) #Mediana dos valores

notas.notas.plot(kind='hist') #Modo de gráfico

notas.notas.describe() #Da uma descrição dos danos

import seaborn as sns  #Importando o Seaborn

sns.boxplot(notas.notas)  #Plotando um gráfico na forma de box

filmes = pd.read_csv("movies.csv")  #Lendo o arquivo csv
filmes.columns = ["filmeId", "titulo", "generos"]  #Trocando os nomes das colunas
filmes.head()

notas.query("filmeId==1").notas.mean() #Analisando a nota média de um filme específico

medias_por_filme = notas.groupby("filmeId").mean().notas  #Agrupando por ID e fazendo a média das notas
medias_por_filme

medias_por_filme.plot(kind='hist') #Plotando do tipo histograma

sns.boxplot(medias_por_filme) #Plotando do tipo box

sns.distplot(medias_por_filme, bins=10) #Bins é a quantidade de quebras de gráfico

import matplotlib.pyplot as plt  #Importando o matplotlib

plt.hist(medias_por_filme)
plt.title("Histograma das médias dos filmes")  #Alterando o título do gráfico

tmdb = pd.read_csv("tmdb_5000_movies.csv")  #Lendo o arquivo csv
tmdb.head()

tmdb.original_language.unique()  #Mostrando os valores presentes na coluna

"""#Variaveis
#budget -> orçamento -> quantitativa continuo
#quantidade de votos -> 1, 2, 3, 4, ..., não tem 2,5
#notas de filmes, 0.5, 1.0, 1.5, ... nao tem 2.7
"""

tmdb["original_language"].value_counts().index #Conta quantas vezes aparecem cada lingua, mas só printa o index

tmdb["original_language"].value_counts().values #Conta quantas vezes aparecem cada lingua, e só aparece os valores

contagem_linguas = tmdb["original_language"].value_counts().to_frame().reset_index() #Cria um DataFrame com as linguas e quantidade que cada uma aparece, reset_index() para criar outra coluna
contagem_linguas.columns = ["idioma", "quant"] #Trocando o nome das colunas
contagem_linguas.head()

sns.barplot(x = "idioma", y = "quant", data = contagem_linguas) #Maneira de plotar, baixo nível

sns.catplot(x = "original_language", kind="count", data = tmdb) #Maneira de plotar, alto nível, mais direta

plt.pie(contagem_linguas.quant, labels = contagem_linguas.idioma) #Gráfico de pizza

total_por_lingua = tmdb.original_language.value_counts()
total_geral = total_por_lingua.sum()
total_de_ingles = total_por_lingua.loc["en"] #Total de resultados em inglês 
total_resto = total_geral - total_de_ingles
#Separar inglês do resto dos idiomas

#Criando um data frame com os valores de inglês e outros
dados = {
    'lingua' : ['ingles', 'outros'],
    'total' : [total_de_ingles, total_resto]
}
dados = pd.DataFrame(dados)

sns.barplot(x = "lingua", y = "total", data = dados) #Plotando os gráficos

plt.pie(dados.total,labels = dados.lingua) #Não é muito bom para ter noção de grandeza

total_por_lingua_outros = tmdb.query("original_language != 'en'").original_language.value_counts()
filmes_diferentes_de_ingles = tmdb.query("original_language != 'en'")
sns.catplot(x = "original_language", kind="count", data = filmes_diferentes_de_ingles, aspect=2, palette="dark:salmon", order=total_por_lingua_outros.index)  #Fazendo um catplot com contagem, aspect para deixar
#o gráfico retangular, palette para mudar a cor das colunas do gráfico e order para ordernar em order decrescente

filmes.head(2)

notas_toy_story = notas.query("filmeId == 1")
notas_jumanji = notas.query("filmeId == 2")
print(len(notas_toy_story), len(notas_jumanji))  #Quantidade de notas em cada filme

print("Nota média do Toy Story é: %.2f" % notas_toy_story.notas.mean())   #Calculando a média de notas dos dois filmes
print("Nota média do Jumanji é: %.2f" % notas_jumanji.notas.mean())

print("Nota mediana do Toy Story é: %.2f" % notas_toy_story.notas.median())   #Calculando a mediana de notas dos dois filmes
print("Nota mediana do Jumanji é: %.2f" % notas_jumanji.notas.median())

import numpy as np  #Importando o Numpy

filme1 = np.append(np.array([2.5] * 10), np.array([3.5] * 10))  #Append para adicionar um array em outro
filme2 = np.append(np.array([1] * 10), np.array([5] * 10))
print(filme1.mean(), filme2.mean())
print(np.std(filme1), np.std(filme2))  #STD cria a distributiva
print(np.median(filme1), np.median(filme2))
#Mostrando as mesmas médias e medianas, mas com notas bem diferentes

plt.hist(filme1)
plt.hist(filme2)

plt.boxplot([filme1, filme2])

plt.boxplot([notas_toy_story.notas, notas_jumanji.notas])

sns.boxplot(x = "filmeId", y = "notas", data = notas.query("filmeId in [1,2,3,4]"))  #Mudando os eixos e passando mais de um filme para o gráfico

print(notas_jumanji.notas.std(), notas_toy_story.notas.std())