# MÓDULO ESTRUTURA DE DADOS

# 2.1 Listas
# Crie uma lista chamada filmes com o nome dos 10 primeiros filmes mais bem avaliados no site no IMDB utilizando a seguinte estrutura: filmes = [...]
# Simule a movimentação do ranking. Para isso, utilize os métodos insert e pop para trocar a posição do primeiro e do segundo filme da lista.
# Imprima o resultado.
# SITE: https://www.imdb.com/chart/top/

#extraindo os filmes
filmes = ["Um Sonho de Liberdade", "O Poderoso Chefão", "Batman: O Cavaleiro das Trevas", "O Poderoso Chefão: Parte II", "12 Homens e uma Sentença", "O Senhor dos Anéis: O Retorno do Rei", "A Lista de Schindler", "Pulp Fiction: Tempo de Violência", "O Senhor dos Anéis: A Sociedade do Anel", "Três Homens em Conflito"]
print(filmes)

#utilizando o insert
filmes.insert(0, "O Poderoso Chefão")
filmes.pop(2)
print(filmes)



# -----------
# 2.2 Conjuntos
# De alguma forma, obtivemos uma lista de filmes com valores duplicados.
# Utilize a conversão para conjunto e, em seguida, novamente para lista para remover os duplicados. Armazene o resultado de volta na variável filmes.
# Imprima o resultado.

filmes = [
    'The Shawshank Redemption',
    'The Godfather',
    'The Dark Knight',
    'The Godfather Part II',
    'The Godfather',
    '12 Angry Men',
    'Schindler\'s List',
    'The Lord of the Rings: The Return of the King',
    'Pulp Fiction',
    'The Shawshank Redemption',
    'The Lord of the Rings: The Fellowship of the Ring',
    'The Good, the Bad and the Ugly',
    'Pulp Fiction'
]
# --
print(filmes)
print(len(filmes))

filmes = list(set(filmes))
print(filmes)
print(len(filmes))

# ------------------------


# 2.3 Dicionários
# Neste momento, repita o passo a passo de criação da lista feita anteriormente: uma lista chamada filmes com o nome dos 10 primeiros filmes mais bem avaliados no site no IMDB. 
# Adicione mais informações a essa estrutura de dados com o ano e a sinopse de cada filme.
# Os elementos da lista filmes devem ser dicionários no seguinte formato:
# {'nome': <nome-do-filme>, 'ano': <ano do filme>, 'sinopse': <sinopse do filme>}

filmes = [
    {'nome': "Um Sonho de Liberdade", 'ano': 1994, 'sinopse': "Dois homens presos se reúnem ao longo de vários anos, encontrando consolo e eventual redenção através de atos de decência comum."},

    {'nome': "O Poderoso Chefão", 'ano': 1972, 'sinopse': "O patriarca idoso de uma dinastia do crime organizado transfere o controle de seu império clandestino para seu filho relutante."},

    {'nome': "Batman: O Cavaleiro das Trevas", 'ano': 2008, 'sinopse': "Agora com a ajuda do tenente Jim Gordon e do promotor público Harvey Dent, Batman tem tudo para banir o crime de Gotham City de uma vez por todas. Mas em breve, os três serão vítimas do Coringa, que pretende lançar Gotham em uma anarquia."},

    {'nome': "O Poderoso Chefão: Parte II", 'ano': 1974, 'sinopse': "Em 1950, Michael Corleone, agora à frente da família, tenta expandir o negócio do crime a Las Vegas, Los Angeles e Cuba. Paralelamente, é revelada a história de Vito Corleone, e de como saiu da Sicília e chegou a Nova Iorque."},

    {'nome': "12 Homens e uma Sentença", 'ano': 1957, 'sinopse': "O julgamento de um assassinato em Nova Iorque é frustrado por um único membro, cujo ceticismo força o júri a considerar cuidadosamente as evidências antes de dar o veredito."},

    {'nome': "O Senhor dos Anéis: O Retorno do Rei", 'ano': 2003, 'sinopse': "Gandalf e Aragorn lideram o Mundo dos Homens contra o exército de Sauron para desviar o olhar de Frodo e Sam quando eles se aproximam á Montanha da Perdição com o Um Anel."},

    {'nome': "A Lista de Schindler", 'ano': 1993, 'sinopse': "Na Polônia ocupada pelos alemães durante a Segunda Guerra Mundial, o industrial Oskar Schindler começa a ser preocupar com seus trabalhadores judeus depois de testemunhar sua perseguição pelos nazistas."},

    {'nome': "Pulp Fiction: Tempo de Violência", 'ano': 1994, 'sinopse': "As vidas de dois assassinos da máfia, um boxeador, um gângster e sua esposa, e um par de bandidos se entrelaçam em quatro histórias de violência e redenção.."},

    {'nome': "O Senhor dos Anéis: A Sociedade do Anel", 'ano': 2001, 'sinopse': "Um manso hobbit do Condado e oito companheiros partem em uma jornada para destruir o poderoso Um Anel e salvar a Terra-média das Trevas."},

    {'nome': "Três Homens em Conflito", 'ano': 1966, 'sinopse': "Um impostor se junta com dois homens para encontrar fortuna num remoto cemitério."}
]

print(filmes)