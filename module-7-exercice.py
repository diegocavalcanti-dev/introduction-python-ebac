# Nesta atividade você vai utilizar a base de dados de ações da bolsa de valores dos EUA, a Dow Jones. Os dados estão disponíveis para download no link:

# https://archive.ics.uci.edu/ml/datasets/Dow+Jones+Index

# Vamos utilizar o pacote wget para fazer o download dos dados.

# 1ª Parte:
# Instalando o pacote wget na versão 3.2.

# !pip install wget==3.2
# 2ª Parte:


# Fazendo o download dos dados no arquivo compactado dados.zip.

# import wget
# wget.download(url='https://archive.ics.uci.edu/ml/machine-learning-databases/00312/dow_jones_index.zip', out='./dados.zip')
# 3ª Parte:

# Descompactando os dados na pasta dados com o pacote nativo zipfile.

# import zipfile
# with zipfile.ZipFile('./dados.zip', 'r') as fp:
#   fp.extractall('./dados')
# 4ª Parte:

# Verifique a pasta dados criada, ela deve conter dois arquivos:

# dow_jones_index.data: um arquivo com os dados;
# dow_jones_index.names: um arquivo com a descrição completa dos dados.
# É possível observar que o arquivo de dados é um arquivo separado por vírgulas, o famoso csv. Vamos renomear o arquivo de dados para que ele tenha a extensão csv com o pacote nativo os.

# ﻿5ª Parte:

# Renomeando o arquivo com o pacote nativo os.

# import os
# os.rename('./dados/dow_jones_index.data', './dados/dow_jones_index.csv')
# Pronto! Abra o arquivo e o Google Colab irá apresentar uma visualização bem legal dos dados.
# 1º Exercício: Pandas
# Para processar os dados, vamos utilizar o pacote pandas na versão 1.5.3. A documentação completa por ser encontrada no link:

# https://pandas.pydata.org/docs/

# !pip install pandas==1.5.3
# Vamos importar o pacote com o apelido (alias) pd.

# import pandas as pd
# Estamos prontos para ler o arquivo.

# df = pd.read_csv('./dados/dow_jones_index.csv')
# O pandas trabalha com o conceito de dataframe, uma estrutura de dados com muitos métodos e atributos que aceleram o processamento de dados. Alguns exemplos:

# Visualizando as n primeiras linhas:

# df.head(n=10)
# Visualizando o nome das colunas:

# df.columns.to_list()
# Verificando o número de linhas e colunas:

# linhas, colunas = df.shape
# print(f'Número de linhas: {linhas}')
# print(f'Número de colunas: {colunas}')
# Vamos selecionar os valores de abertura, fechamento, máximo e mínimo das ações do McDonalds, listado na Dow Jones como MCD:

# a. Selecionando as linha do dataframe original df em que a coluna stock é igual a MCD:

# df_mcd = df[df['stock'] == 'MCD']
# b. Selecionando apenas as colunas de data e valores de ações:

# df_mcd = df_mcd[['date', 'open', 'high', 'low', 'close']]
# O problema é que as colunas com os valores possuem o caractere $ e são do tipo texto (object no pandas).

# df_mcd.head(n=10)
# df_mcd.dtypes
# c. Vamos limpar as colunas com o método apply, que permite a aplicação de uma função anônima (lambda) qualquer. A função lambda remove o caracter $ e faz a conversão do tipo de str para float.

# for col in ['open', 'high', 'low', 'close']:
#   df_mcd[col] = df_mcd[col].apply(lambda value: float(value.split(sep='$')[-1]))
# d. Verifique novamente os dados e seus tipos.

# df_mcd.head(n=10)
# df_mcd.dtypes
# Agora é a sua vez!
# Conduza o mesmo processo para extrair e tratar os dados da empresa Coca-Cola (stock column igual a KO).

# a. Selecione as linhas do dataframe original df em que a coluna stock é igual a KO.

# Vamos selecionar os valores de abertura, fechamento, máximo e mínimo das ações da empresa Coca-Cola, listado na Dow Jones como KO:

# b. Selecione apenas as colunas de data e valores de ações.

# O problema é que as colunas com os valores possuem o caractere $ e são do tipo texto (object no pandas).

# c. Limpe as colunas com o método apply, que permite a aplicação de uma função anônima (lambda) qualquer. A função lambda remove o caracter $ e faz a conversão do tipo de str para float.

# d. Verifique novamente os dados e seus tipos.

# e. Explore os dados visualmente.

# 2º Exercício: Seaborn
# Para visualizar os dados, vamos utilizar o pacote seaborn na versão 0.13.2. A documentação completa por ser encontrada no link:

# https://seaborn.pydata.org/

# !pip install seaborn==0.13.2
# Importe o pacote com o apelido (alias) sns.

# import seaborn as sns
# Vamos visualizar os valores de abertura das ações ao longo do tempo.

# plot = sns.lineplot(x="date", y="open", data=df_mcd)
# plot.tick_params(axis='x', labelrotation = 45)
# Para facilitar a comparação, vamos visualizar os quatro valores no mesmo gráfico.
# plot = sns.lineplot(x="date", y="value", hue='variable', data=pd.melt(df_mcd, ['date']))
# plot.tick_params(axis='x', labelrotation = 45)
# Para finalizar, vamos salvar o gráfico numa figura.
# plot.figure.savefig("./mcd.png")
# Agora é a sua vez!
# a. Faça o gráfico acima para a empresa Coca-Cola e salve a imagem com o nome ko.png.
# b. Visualize os valores de abertura das ações ao longo do tempo.
# c. Visualize os valores de fechamento das ações ao longo do tempo.
# d. Para facilitar a comparação, visualize os quatro valores no mesmo gráfico.
# e. Para finalizar, salve o gráfico numa figura.
# f. Analise as duas imagens e escreva pelo menos um insight que você consegue extrair dos dados. Fique a vontade para escrever quantos insights você quiser.


# -------------------------------------

# 7.1 Pandas
# Neste exercício vamos utilizar a base de dados de ações da bolsa de valores dos EUA, a Dow Jones. Para processar os dados, vamos utilizar o pacote `pandas`. A documentação completa por ser encontrada neste link.
# Todas as bibliotecas já estão instaladas e o arquivo CSV já existe no caminho /data/dow_jones_index.csv
# Para tratar os dados, você deve:
# Filtrar os dados para utilizar apenas os dados da empresa Coca-cola (coluna stock com o valor KO).
# Selecionar os valores de abertura, fechamento, máximo e mínimo das ações da empresa Coca-Cola.
# Limpar as colunas, retirando o caractere $ e convertendo os valores de string para float.
# Certifique-se que o Dataframe final esteja armazenado na variável df_coke
# Obs: No Material de Apoio da aula existe um Jupyter Notebook com explicações e exemplos. Veja o material antes de resolver o exercício.


import pandas as pd

df = pd.read_csv('/data/dow_jones_index.csv')

# Crie um Dataframe filtrado, selecionando as linha do dataframe original df em que a coluna stock é igual a KO.
df_coke = df[df['stock'] == 'KO']

# Selecione apenas as colunas de data e valores de ações: ['date', 'open', 'high', 'low', 'close'].
df_coke = df_coke[['date', 'open', 'high', 'low', 'close']]

# Limpe as colunas com o método `apply`, que permite a aplicação de uma função anônima (`lambda`) qualquer. A função `lambda` deve remover o caracter `$` e fazer a conversão do tipo de `str` para `float`.
for col in ['open', 'high', 'low', 'close']:
    df_coke[col] = df_coke[col].apply(lambda value: float(value.split(sep='$')[-1]))

# print the types
print(df_coke.dtypes)
df_coke.head(n=10)  # Visualizando as primeiras 10 linhas



# -----------------------------------------------------------


# 7.2 Seaborn parte 1
# Para visualizar os dados, vamos utilizar o pacote seaborn na versão 0.13.2. A documentação completa por ser encontrada neste https://seaborn.pydata.org/.
# Todas as bibliotecas necessárias já estão instaladas. O arquivo /data/df_coke.csv contém o resultado da Parte 1 deste exercício, com os dados já filtrados e convertidos para o tipo float.
# Crie um gráfico de linha (sns.lineplot()) que demonstre a visualização da abertura das ações (coluna 'open') ao longo do tempo.
# Obs: para visualizar seu gráfico, utilize o comando plt.show().
# Seu gráfico deve ser semelhante a esse:

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Carregar os dados do arquivo CSV
df_coke = pd.read_csv('/data/df_coke.csv', index_col=0)

# Criar a figura
fig, axs = plt.subplots(1, figsize=(8, 8))

# Gerar o gráfico de linha para os valores de abertura (coluna 'open')
plot = sns.lineplot(x="date", y="open", data=df_coke)

# Ajustar a rotação dos rótulos do eixo x
plot.tick_params(axis='x', labelrotation=45)

# Exibir o gráfico
plt.show()