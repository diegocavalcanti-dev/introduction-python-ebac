# Módulo 8 - PYTHON Tratamento de erros

# 8.1 Erros de sintaxe 01: Laços de repetição
# Identifique o erro de sintaxe nos trechos de código abaixo e corrija-os para que o trecho de código funcione.

# Execute o código inicial para ver a mensagem de erro. Altere o mínimo necessário para deixar o código funcionando.

# código corrigido

credito = {'123': 750, '456': 812, '789': 980}

for chave, valor in credito.items():
	print(f"Para o documento {chave}, o valor do escore de crédito é {valor}.")
 

# ------------------------------

# 8.2 Erros de sintaxe 02: Funções
# Identifique o erro de sintaxe nos trechos de código abaixo e corrija-os para que o trecho de código funcione.
# Execute o código inicial para ver a mensagem de erro. Altere o mínimo necessário para deixar o código funcionando.

def pi_func():
    return 3.14159265359

pi_var = pi_func()
print(pi_var)


# ---------------------------------

# 8.3 Erros de sintaxe 03: Programação Funcional
# Identifique o erro de sintaxe nos trechos de código abaixo e corrija-os para que o trecho de código funcione.
# Execute o código inicial para ver a mensagem de erro. Altere o mínimo necessário para deixar o código funcionando.


emails = ['andre.perez@gmail.com', 'andre.perez@live.com', 'andre.perez@yahoo.com']
provedor_da_google = lambda email: 'gmail' in email

emails_google = filter(provedor_da_google, emails)
print(list(emails_google))


# 8.4 Erros de sintaxe 04: Programação orientação a objetos
# Identifique o erro de sintaxe nos trechos de código abaixo e corrija-os para que o trecho de código funcione.
# Execute o código inicial para ver a mensagem de erro. Altere o mínimo necessário para deixar o código funcionando.

class Pessoa(object):
	def __init__(self, nome: str, idade: int, documento: str):
		self.nome = nome
		self.idade = idade
		self.documento = documento

andre = Pessoa(nome="Andre", idade=30, documento="123")


# --------------------------------------

# 8.5 Erros em tempo de execução
# O código abaixo deve calcular o total emprestado por cada vendedor mas está "estourando" a exceção ValueError devido a um erro no conjunto de dados. Utilize a estrutura try-except para garantir que o código seja executado com sucesso.
# Identique o bloco que código que pode gerar a exceção e utilize try e except de modo que a operação que pode causar o problema seja colocada dentro do bloco try, e o código que trata a exceção seja escrito dentro do bloco except.
# Trate a Exception e armazene em uma variável chamada error.
# Dentro do except, utilize o método replace() para remover as aspas do conjunto de dados linha_elementos[1].
# Obs: Através do replace() para remover um caractere, o método vai substituir cada caractere por vazio.
# O resultado final deve ser a impressão da seguinte lista:
# {'104271': 448.0}
# {'21476': 2480.1000000000004}
# {'87440': 940.8000000000001}
# {'15980': 4848.0}
# {'215906': 11060.0}
# {'33696': 5542.6}
# {'33893': 6720.0}
# {'214946': 74718.0}
# {'123974': 4043.9}
# {'225870': 8078.0}


def valor_total_emprestimo(valor: float, quantidade: int) -> float:
	return valor * quantidade

emprestimos = []

with open(file='/data/credito.csv', mode='r', encoding='utf8') as fp:
	fp.readline() # cabeçalho
	linha = fp.readline()
	while linha:
		linha_emprestimo = {}
		linha_elementos = linha.strip().split(sep=',')
		linha_emprestimo['id_vendedor'] = linha_elementos[0]
		linha_emprestimo['quantidade_emprestimos'] = int(linha_elementos[2])
		linha_emprestimo['data'] = linha_elementos[3]
		emprestimos.append(linha_emprestimo)

		try:
			linha_emprestimo['valor_emprestimos'] = float(linha_elementos[1])
		except ValueError as e:
			error = str(e)
			linha_emprestimo['valor_emprestimos'] = float(linha_elementos[1].replace('"', ''))
		finally:
			linha = fp.readline()

emprestimos_total = []
for emprestimo in emprestimos:
	valor_total = valor_total_emprestimo(valor=emprestimo['valor_emprestimos'], quantidade=emprestimo['quantidade_emprestimos'])
	emprestimos_total.append({emprestimo['id_vendedor']: valor_total})

for emprestimo_total in emprestimos_total:
	print(emprestimo_total)