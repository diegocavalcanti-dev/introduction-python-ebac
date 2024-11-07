# Módulo Programação funcional

# 5.1 Função `map`
# Aplique a função map na lista de emprestimos para extrair os valores da chave valor_emprestimos na variável valor_emprestimos_map.
# Ainda na função map, faça também a conversão de str para float.
# Tranforme valor_emprestimos_map em lista e armazene na variável valor_emprestimos_lista.
# Imprima a variável valor_emprestimos_lista.
# Veja abaixo a estrutura do arquivo credito.csv:

# id_vendedor,valor_emprestimos,quantidade_emprestimos,data
# 104271,448.0,1,20161208
# 21476,826.7,3,20161208
# 87440,313.6,3,20161208
# 15980,-8008.0,6,20161208
# 215906,2212.0,5,20161208
# 33696,2771.3,2,20161208
# 33893,2240.0,3,20161208
# 214946,-4151.0,18,20161208
# 123974,2021.95,2,20161208
# 225870,4039.0,2,20161208

emprestimos = []
with open(file='../../data/credito.csv', mode='r', encoding='utf8') as fp:
	fp.readline() # cabeçalho
	linha = fp.readline()
	while linha:
		linha_emprestimo = {}
		linha_elementos = linha.strip().split(sep=',')
		linha_emprestimo['id_vendedor'] = linha_elementos[0]
		linha_emprestimo['valor_emprestimos'] = linha_elementos[1]
		linha_emprestimo['quantidade_emprestimos'] = linha_elementos[2]
		linha_emprestimo['data'] = linha_elementos[3]
		emprestimos.append(linha_emprestimo)
		linha = fp.readline()

# Escreva seu código abaixo

valor_emprestimos_map = map(lambda emprestimo: float(emprestimo['valor_emprestimos']), emprestimos)

valor_emprestimos_lista = list(valor_emprestimos_map)

print(valor_emprestimos_lista)


# -----------------------------------------------------------------

# 5.2 Função `filter`
# Aplique a função filter na lista de valor_emprestimos_lista para filtrar apenas os valores maiores que zero (os valores negativas são erros na base de dados). Atribua o resulta a variável valor_emprestimos_filtrado.
# Transforme o resultado numa lista e armazene em valor_emprestimos_filtrado_lista.
# Imprima a variável valor_emprestimos_filtrado_lista.

emprestimos = []
with open(file='../../data/credito.csv', mode='r', encoding='utf8') as fp:
	fp.readline() # cabeçalho
	linha = fp.readline()
	while linha:
		linha_emprestimo = {}
		linha_elementos = linha.strip().split(sep=',')
		linha_emprestimo['id_vendedor'] = linha_elementos[0]
		linha_emprestimo['valor_emprestimos'] = linha_elementos[1]
		linha_emprestimo['quantidade_emprestimos'] = linha_elementos[2]
		linha_emprestimo['data'] = linha_elementos[3]
		emprestimos.append(linha_emprestimo)
		linha = fp.readline()

valor_emprestimos_lista = list(map(lambda x: float(x['valor_emprestimos']), emprestimos))

# Escreva seu código abaixo

valor_emprestimos_filtrado = filter(lambda x: x > 0, valor_emprestimos_lista)

valor_emprestimos_filtrado_lista = list(valor_emprestimos_filtrado)

print(valor_emprestimos_filtrado_lista)



# -----------------------------------------------------------------

# 5.3 Função `reduce` para extrair a média aritmética
# Aplique a função reduce para extrair a média aritimética (veja as dicas) dos elementos da lista valor_emprestimos_lista_filtrado e armazene na variavel media_valor_emprestimos.
# Para calcular o tamanho da lista, isto é, a quantidade de elementos, utilize a função len() e dentro do argumento da função coloque a lista valor_emprestimos_lista_filtrada.
# Imprima a variável media_valor_emprestimos.


from functools import reduce

emprestimos = []
with open(file='../../data/credito.csv', mode='r', encoding='utf8') as fp:
	fp.readline() # cabeçalho
	linha = fp.readline()
	while linha:
		linha_emprestimo = {}
		linha_elementos = linha.strip().split(sep=',')
		linha_emprestimo['id_vendedor'] = linha_elementos[0]
		linha_emprestimo['valor_emprestimos'] = linha_elementos[1]
		linha_emprestimo['quantidade_emprestimos'] = linha_elementos[2]
		linha_emprestimo['data'] = linha_elementos[3]
		emprestimos.append(linha_emprestimo)
		linha = fp.readline()

valor_emprestimos_lista = list(map(lambda x: float(x['valor_emprestimos']), emprestimos))
valor_emprestimos_filtrado = list(filter(lambda x: x > 0, valor_emprestimos_lista))

# Escreva seu código abaixo

soma_valores = reduce(lambda x, y: x + y, valor_emprestimos_filtrado)

# Calculando a média
media_valor_emprestimos = soma_valores / len(valor_emprestimos_filtrado)

print(media_valor_emprestimos)



# --------------------------------------------------------------------



# 5.4 Função `reduce` para extrair o desvio padrão amostral
# Neste exercício você deverá aplicar uma combinação de funções para calcular o desvio padrão amostral da coluna valor_emprestimos.
# Segundo a Wikipedia, desvio padrão é:
# é uma medida de dispersão em torno da média populacional de uma variável aleatória. O termo possui também uma acepção específica no campo da estatística, na qual também é chamado de desvio padrão amostral (comumente representado pela letra latina s s) e indica uma medida de dispersão dos dados em torno de média amostral.
# Para compreender melhor esse conceito, vamos usar os preços de sorvetes como exemplo:
# Sorvete 1: R$ 2,00
# Sorvete 2: R$ 2,50
# Sorvete 3: R$ 3,00
# Sorvete 4: R$ 3,50
# O preço médio desses sorvetes é de R$ 2,75.
# Agora, se os preços estiverem perto de R$ 2,75, o desvio padrão é pequeno, o que significa que os preços não são muito diferentes uns dos outros.
# Mas se os preços estiverem longe de R$ 2,75, o desvio padrão é grande, o que indica que alguns sorvetes são bem mais caros ou mais baratos do que a média.
# A correção de Bessel é como um ajuste que usamos quando estamos olhando apenas para alguns sorvetes em vez de todos os sorvetes do mundo. Isso nos ajuda a ter uma ideia melhor de quanto os preços dos sorvetes podem variar no geral.
# Para o cálculo, então, partimos do preço médio de todos os sorvetes, que é R$ 2,75.
# Agora, queremos saber o quanto os preços são diferentes desse valor médio. Para fazer isso, subtraímos o preço médio de cada sorvete e depois elevamos o resultado ao quadrado (para não termos números negativos).
# Então, teríamos algo assim:
# (2,00 - 2,75)² = 0,5625
# (2,50 - 2,75)² = 0,0625
# (3,00 - 2,75)² = 0,0625
# (3,50 - 2,75)² = 0,5625
# Agora, somamos todos esses valores juntos: 0,5625 + 0,0625 + 0,0625 + 0,5625 = 1,25.
# Finalmente, dividimos esse resultado pelo número de sorvetes que temos (neste caso, 4), menos 1 (por conta da correção de Bessel, explicada anteriormente). Ficaria assim: 1,25 ÷ (4 - 1) = 0,4167.
# A raiz quadrada de 0,4167 é aproximadamente 0,645. Isso é o nosso desvio padrão, e ele nos diz o quanto os preços dos sorvetes variam em relação ao preço médio de R$ 2,75. Quanto maior o desvio padrão, mais diferentes são os preços dos sorvetes.
# Em resumo, o cálculo do desvio padrão amostral segue os seguintes passos:
# Calcule a média aritmética da amostra (conforme exercício anterior).
# Calcule a diferença entre cada valor e a média. Eleve o resultado ao quadrado (para elimnar valores negativos).
# Some todos os valores calculados.
# Divida a soma pelo número de elementos menos 1 e extraia a raiz quadrada do resultado.
# Atente para as instruções do que deve conter no seu código:
# A média aritmética já foi calculada anteriormente e está representada na variável media_valor_emprestimos.
# Utilize a função map para calcular o quadrado das diferenças e armazene na variável quadrado_diferencas. (Passo 2)
# Utilize a função reduce para calcular a soma dos quadrados das diferenças e armazene na variável soma_quadrado_diferencas. (Passo 3)
# Cálculo a média aritmética amostral e armazene na variável desvio_padrao_emprestimos. (Passo 4)


from functools import reduce

emprestimos = []
with open(file='../../data/credito.csv', mode='r', encoding='utf8') as fp:
	fp.readline() # cabeçalho
	linha = fp.readline()
	while linha:
		linha_emprestimo = {}
		linha_elementos = linha.strip().split(sep=',')
		linha_emprestimo['id_vendedor'] = linha_elementos[0]
		linha_emprestimo['valor_emprestimos'] = linha_elementos[1]
		linha_emprestimo['quantidade_emprestimos'] = linha_elementos[2]
		linha_emprestimo['data'] = linha_elementos[3]
		emprestimos.append(linha_emprestimo)
		linha = fp.readline()

valor_emprestimos_lista = list(map(lambda x: float(x['valor_emprestimos']), emprestimos))
valor_emprestimos_filtrado = list(filter(lambda x: x > 0, valor_emprestimos_lista))
media_aritmetica = reduce(lambda x, y: x + y, valor_emprestimos_filtrado) / len(valor_emprestimos_filtrado)

# Escreva seu código abaixo

# Passo 2: Calcular o quadrado das diferenças entre cada valor e a média
quadrado_diferencas = map(lambda x: (x - media_aritmetica) ** 2, valor_emprestimos_filtrado)

# Passo 3: Calcular a soma dos quadrados das diferenças
soma_quadrado_diferencas = reduce(lambda x, y: x + y, quadrado_diferencas)

# Passo 4: Calcular o desvio padrão amostral
desvio_padrao_emprestimos = (soma_quadrado_diferencas / (len(valor_emprestimos_filtrado) - 1)) ** 0.5

# Imprimir o resultado
print(desvio_padrao_emprestimos)
