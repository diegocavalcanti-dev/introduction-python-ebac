# MÓDULO FLUXO CONDICIONAL & REPETIÇÃO

# 3.1 Estrutura condicional for / in
# Na lista propaganda_online dada no editor ao lado, estão presente os dados de usuários que acessaram um determinado site e se o mesmo clicou em uma propaganda.
# Imprima os valores de idade e tempo_gasto_site, utilizando a estrutura "for / in". Os valores devem ser impressos na mesma linha, para cada dado da lista.
# Obs: Se atenha apenas aos valores solicitados. Qualquer saída que tiver informações extras será considerada um erro.

# LISTA: 
propaganda_online = [
	{'tempo_gasto_site': 68.95, 'idade': 35, 'renda_area': 61833.90, 'tempo_gasto_internet': 256.09, 'cidade': 'Wrightburgh', 'pais': 'Tunisia', 'clicou_no_ad': 0},
	{'tempo_gasto_site': 80.23, 'idade': 31, 'renda_area': 68441.85, 'tempo_gasto_internet': 193.77, 'cidade': 'West Jodi', 'pais': 'Nauru', 'clicou_no_ad': 0},
	{'tempo_gasto_site': 69.47, 'idade': 26, 'renda_area': 59785.94, 'tempo_gasto_internet': 236.50, 'cidade': 'Davidton', 'pais': 'San Marino', 'clicou_no_ad': 0},
	{'tempo_gasto_site': 68.37, 'idade': 35, 'renda_area': 73889.99, 'tempo_gasto_internet': 225.58, 'cidade': 'South Manuel', 'pais': 'Iceland', 'clicou_no_ad': 0},
	{'tempo_gasto_site': 88.91, 'idade': 33, 'renda_area': 53852.85, 'tempo_gasto_internet': 208.36, 'cidade': 'Brandonstad', 'pais': 'Myanmar', 'clicou_no_ad': 0},
	{'tempo_gasto_site': None, 'idade': 48, 'renda_area': 24593.33, 'tempo_gasto_internet': 131.76, 'cidade': 'Port Jefferybury', 'pais': 'Australia', 'clicou_no_ad': 1},
	{'tempo_gasto_site': 74.53, 'idade': 30, 'renda_area': 68862.00, 'tempo_gasto_internet': 221.51, 'cidade': 'West Colin', 'pais': 'Grenada'},
	{'tempo_gasto_site': 69.88, 'idade': 20, 'renda_area': 55642.32, 'tempo_gasto_internet': 183.82, 'cidade': 'Ramirezton', 'pais': 'Ghana', 'clicou_no_ad': 0}
]

# Escreva seu código abaixo
for dado_de_usuario in propaganda_online:
	print(f'A idade do usuário é {dado_de_usuario["idade"]} anos e o tempo gasto no site é {dado_de_usuario["tempo_gasto_site"]} minutos.')


# 3.2 Estrutura condicional if / else
# Utilize a estrutura if/else para imprimir a cidade dos usuários que gastaram mais de 200 horas de tempo na internet.

for dado_de_usuario in propaganda_online:
    if dado_de_usuario['tempo_gasto_internet'] >= 200:
        print('\n') #usado para pular linha
        print(dado_de_usuario['cidade'])
        

# 3.3 Estrutura condicional try / except
# Utilize a estrutura try/except para imprimir as cidades dos usuários que passaram mais de 70 segundos no site. 
# Realize o tratamento de exceções dentro da execução da iteração dos elementos da lista. Trate a exceção atribuindo-a à variável error.


# lista:
propaganda_online = [
	{'tempo_gasto_site': 68.95, 'idade': 35, 'renda_area': 61833.90, 'tempo_gasto_internet': 256.09, 'cidade': 'Wrightburgh', 'pais': 'Tunisia', 'clicou_no_ad': 0},
	{'tempo_gasto_site': 80.23, 'idade': 31, 'renda_area': 68441.85, 'tempo_gasto_internet': 193.77, 'cidade': 'West Jodi', 'pais': 'Nauru', 'clicou_no_ad': 0},
	{'tempo_gasto_site': 69.47, 'idade': 26, 'renda_area': 59785.94, 'tempo_gasto_internet': 236.50, 'cidade': 'Davidton', 'pais': 'San Marino', 'clicou_no_ad': 0},
	{'tempo_gasto_site': 68.37, 'idade': 35, 'renda_area': 73889.99, 'tempo_gasto_internet': 225.58, 'cidade': 'South Manuel', 'pais': 'Iceland', 'clicou_no_ad': 0},
	{'tempo_gasto_site': 88.91, 'idade': 33, 'renda_area': 53852.85, 'tempo_gasto_internet': 208.36, 'cidade': 'Brandonstad', 'pais': 'Myanmar', 'clicou_no_ad': 0},
	{'tempo_gasto_site': None, 'idade': 48, 'renda_area': 24593.33, 'tempo_gasto_internet': 131.76, 'cidade': 'Port Jefferybury', 'pais': 'Australia', 'clicou_no_ad': 1},
	{'tempo_gasto_site': 74.53, 'idade': 30, 'renda_area': 68862.00, 'tempo_gasto_internet': 221.51, 'cidade': 'West Colin', 'pais': 'Grenada'},
	{'tempo_gasto_site': 69.88, 'idade': 20, 'renda_area': 55642.32, 'tempo_gasto_internet': 183.82, 'cidade': 'Ramirezton', 'pais': 'Ghana', 'clicou_no_ad': 0}
]

error = None
for dado_de_usuario in propaganda_online:
    try:
        # Verifica se 'tempo_gasto_site' é maior que 70
        if dado_de_usuario['tempo_gasto_site'] > 70:
            print(dado_de_usuario['cidade'])
    except (TypeError, KeyError) as e:
        # Atribui a exceção à variável error
        error = e
        continue  # Ignore o erro e continue com o próximo registro
        # Trata os casos onde 'tempo_gasto_site' é None ou há outros erros
        continue  # Ignore o erro e continue com o próximo registro
