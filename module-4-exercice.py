# Módulo Arquivos e Funções

# 4.1 Extração de coluna de arquivo csv
# Extraia os valores da coluna "valor_venda" e armazena em uma lista na variável valor_venda .
# Siga os passos apresentados pelas linhas de comentários no editor de código.
# Imprima a variável valor_venda utilizando a função print()

# Abaixo está o conteúdo do arquivo CSV:

# id,valor_venda,valor_manutencao,portas,pessoas,porta_malas
# 1,vhigh,med,2,2,small
# 2,med,vhigh,2,2,small
# 3,low,vhigh,2,2,small
# 4,low,high,2,2,small
# 5,low,high,2,2,small
# 6,low,high,4,4,big
# 7,low,high,4,4,big
# 8,low,med,2,2,small
# 9,low,med,2,2,small
# 10,low,med,2,2,small
# 11,low,med,4,4,big
# 12,low,low,2,2,small
# 13,low,low,4,4,small
# 14,low,low,4,4,med


valor_venda = []

with open(file='../../data/carros.csv', mode='r', encoding='utf8') as arquivo:
	arquivo.readline()
	for linha in arquivo:
		colunas = linha.strip().split(',')
		valor_venda.append(colunas[1])
	print(valor_venda)
 
# --------------------

# 4.2 Função para extração de coluna de arquivo csv
# Complete a função para extração os valores de valor_venda e que retorne uma lista com os valores.
# A função deve ter como parâmetros nome_arquivo e indice_coluna.
# Siga os passos apresentados pelas linhas de comentários no editor de código.

import os

def extrai_coluna_csv(nome_arquivo: str, indice_coluna: int):
    valores_coluna = []

    try:
        with open(f'../../data/{nome_arquivo}', mode='r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            
            for i, linha in enumerate(linhas):
                if i == 0:
                    continue
                colunas = linha.strip().split(',')
                if len(colunas) > indice_coluna:
                    valor = colunas[indice_coluna].strip()
                    if valor:
                        valores_coluna.append(valor)
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não foi encontrado.")
    return valores_coluna 

nome_arquivo = 'carros.csv'
indice_coluna = 3

valores = extrai_coluna_csv(nome_arquivo, indice_coluna)
print(valores)
print(f"Quantidade de elementos: {len(valores)}")


# -------------------

# 4.3 Função para extração de coluna de arquivo csv e conversão de dados
# Complete a função para extração os valores de valor_venda e que retorne uma lista com os valores.
# A função deve ter como parâmetros nome_arquivo, indice_coluna, tipo_dado.
# O parâmetro tipo_dado deve aceitar como argumento os valores "str" ou "int".
# Siga os passos apresentados pelas linhas de comentários no editor de código.

import os

def extrai_coluna_csv(nome_arquivo: str, indice_coluna: int, tipo_dado: str):
    coluna = []
    
    caminho_arquivo = os.path.join('../../data/', nome_arquivo)
    
    with open(caminho_arquivo, mode='r', encoding='utf8') as arquivo:
        cabecalho = arquivo.readline()
        
        for linha in arquivo:
            dados = linha.strip().split(',')
            
            valor = dados[indice_coluna]
            
            if tipo_dado == 'int':
                valor = int(valor)
            elif tipo_dado == 'str':
                valor = str(valor)
            else:
                raise ValueError
            
            coluna.append(valor)

    return coluna

nome_arquivo = 'carros.csv'
indice_coluna = 3  # Exemplo de coluna "valor_venda"
tipo_dado = 'int'  # Tipo de dado que você quer retornar

valores = extrai_coluna_csv(nome_arquivo, indice_coluna, tipo_dado)
print(valores) 
print(f"Quantidade de elementos: {len(valores)}")



# ---------------------

# 4.4 Funções para arquivo txt
# Complete a função para extrair as palavras de uma linha do arquivo txt em uma lista.
# Siga os passos apresentados pelas linhas de comentários no editor de código.

# Veja abaixo o corpo do texto do arquivo .txt:
# Roda Viva
# Chico Buarque

# Tem dias que a gente se sente
# Como quem partiu ou morreu
# A gente estancou de repente
# Ou foi o mundo então que cresceu
# A gente quer ter voz ativa
# No nosso destino mandar
# Mas eis que chega a roda viva
# E carrega o destino pra lá

# Roda mundo, roda-gigante
# Roda moinho, roda pião

# O tempo rodou num instante
# Nas voltas do meu coração
# A gente vai contra a corrente
# Até não poder resistir
# Na volta do barco é que sente
# O quanto deixou de cumprir
# Faz tempo que a gente cultiva
# A mais linda roseira que há
# Mas eis que chega a roda viva
# E carrega a roseira pra lá

# Roda mundo, roda-gigante
# Roda moinho, roda pião

import os

def extrai_linha_txt(nome_arquivo: str, numero_linha: int):
    palavras_linha = []
    caminho_arquivo = os.path.join("../../data", nome_arquivo)
    try:
        with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            if 0 < numero_linha <= len(linhas):
                linha = linhas[numero_linha - 1]
                palavras_linha = linha.split()
                if palavras_linha and linha.endswith('\n'):
                    palavras_linha[-1] += '\n'
            else:
                print(f"Linha {numero_linha} não encontrada. O arquivo tem {len(linhas)} linhas.")
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    return palavras_linha
linha5 = extrai_linha_txt(nome_arquivo='musica.txt', numero_linha=5)
print(linha5)
