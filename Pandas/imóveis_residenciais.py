# -*- coding: utf-8 -*-
"""Imóveis Residenciais

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TtAeK6lYuTwHDS5oB-iHvmQLWwi-CD2w

#Relatório de análise III

Imóveis residenciais
"""

import pandas as pd

dados = pd.read_csv('aluguel.csv', sep = ';')
dados.head()

residencial = dados['Tipo'].drop_duplicates()   #Removendo duplicados
residencial = residencial.tolist()         #Passando o residencial para uma lista
residencial = ['Quitinete', 'Casa', 'Apartamento', 'Casa de Condomínio', 'Casa de Vila']  #Deixando apenas os imóveis residenciais
residencial

selecao = dados['Tipo'].isin(residencial)  #Retorna true ou false caso tenha o item da lista na coluna do df
selecao

dados_residencial = dados[selecao]  #Criando um df novo só com os Tipos selecionados
dados_residencial

resto = dados_residencial['Tipo'].drop_duplicates()  #Conferindo se tem os itens esperados
resto.tolist()

dados_residencial.shape[0] #Verificando a quantidade de linhas

dados_residencial.index = range(1, dados_residencial.shape[0]+1) #Mudando o index, para a ordem correta
dados_residencial.head(10)

"""#Exportando a base de dados"""

dados_residencial.to_csv('aluguel_residencial.csv', sep = ';', index = False)  #Exportando csv

dados_residencial_2 = pd.read_csv('aluguel_residencial.csv', sep = ';')   #Importando o df novo
dados_residencial_2

"""#Relatório de análise IV"""

#Selecione somente os imóveis do tipo Apartamento
selecao = dados['Tipo'] == 'Apartamento'
n1 = selecao = dados[selecao]
print('{} imóveis'.format(n1.shape[0]))
n1.index = range(1, selecao.shape[0]+1)
n1

#Selecione os imóveis classificados com tipos 'Casa', 'Casa de condomínio' e 'Casa de vila'
selecao = (dados['Tipo'] == 'Casa') | (dados['Tipo'] == 'Casa de Condomínio') | (dados['Tipo'] == 'Casa de Vila')
n2 = dados[selecao].shape[0]
print('{} imoveis'.format(n2))

#Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites
selecao = (dados['Area'] >= 60) & (dados['Area'] <= 100)
n3 = dados[selecao].shape[0]
print('{} imóveis'.format(n3))

#Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00
selecao = (dados['Quartos'] >= 4) & (dados['Valor'] < 2000)
n4 = dados[selecao].shape[0]
print('{} imóveis'.format(n4))