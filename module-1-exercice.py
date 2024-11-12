# 1.1

# Olá mundo!
# Lição: Nela, escreva o texto "Olá mundo!", utilize a função print

# Escreva seu código aqui
print("Olá Mundo")


# --------------
# 1.2
# Números
# Use expressões algébricas para calcular (A), (B) e (C) na tabela de ticket médio abaixo:

# 19/01
qtd_total_vendas_1 = 3
ticket_medio_1 = 320.52

# 20/01
valor_total_vendas_2 = 834.47
ticket_medio_2 = 119.21

# 23/01
valor_total_vendas_3 = 15378.12
qtd_total_vendas_3 = 5

# Calcule aqui:
A = ticket_medio_1 * qtd_total_vendas_1
B = valor_total_vendas_2 / ticket_medio_2
C = valor_total_vendas_3 / qtd_total_vendas_3

# Print
print('(A) = ', A)
print('(B) = ', B)
print('(C) = ', C)

# --------------------
# 1.3
# String: Parte 1

# Aplique três métodos distintos na string abaixo.
# cancao = 'Roda mundo, roda gigante, roda moinho, roda pião.'
# Substitua todas as vírgulas por barras /
# Deixe a string em maiúscula
# Encontre a posição da palavra "moinho" na string


cancao = 'Roda mundo, roda gigante, roda moinho, roda pião.'

# Substitua todas as vírgulas por barras /
result1 = cancao.replace(',', '/')
print(result1)

# Deixe a string em maiúscula
result2 = cancao.upper()
print(result2)

# Encontre a posição da palavra "moinho" na string
result3 = cancao.find('moinho')
print(result3)


# ------------
# 1.4
# String: Parte 2

# Extraia da string abaixo o valor da taxa selic na variável selic e o valor do ano na variável ano. Imprima os valores na tela.

# noticia = 'Selic vai a 2,75% e supera expectativas; ' + \ 'é a primeira alta em 6 anos.'

noticia = 'Selic vai a 2,75% e supera expectativas é a primeira alta em 6 anos.'

# Extraindo o valor da Selic
inicio_selic = noticia.find("a ") + 2
fim_selic = noticia.find('%') 
selic = noticia[inicio_selic:fim_selic]

# Extraindo o ano
inicio_ano = noticia.find('em ') + 3
fim_ano = noticia.find(' anos')
ano = noticia[inicio_ano:fim_ano]

# Exibindo os valores
print(f"Selic: {selic}")
print(f"Ano: {ano}")


# ----------------------------------------------
# 1.5
# Booleans
# Utilize a tabela da verdade para responder: qual o valor da variável x?

a = False
b = True
x = not a & b

# True & True = True

not_a = True
b = True
x = (not_a & b)
print(x)