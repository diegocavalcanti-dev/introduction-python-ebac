# Módulo Programação Orientada a Objetos

# 6.1 Classe para ler arquivos de texto
# Crie a classe ArquivoTexto. Ela deve conter os seguintes atributos:
# self.arquivo: Atributo do tipo str com o nome do arquivo;
# self.conteudo: Atributo do tipo list onde cada elemento é uma linha do arquivo;
# A classe também deve conter o seguinte método:
# self.extrair_conteudo: Método que realiza a leitura do arquivo e retorna o conteúdo.
# self.extrair_linha: Método que recebe como parâmetro o número da linha e retorna a linha do conteúdo. Considere a primeira linha como número 1.
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

class ArquivoTexto(object):
    def __init__(self, arquivo: str):
        self.arquivo = arquivo
        self.conteudo = self.extrair_conteudo()
    def extrair_conteudo(self):
        conteudo = []
        try:
            with open(self.arquivo, "r", encoding="utf8") as arquivo:
                conteudo = arquivo.readlines()
        except FileNotFoundError:
            print(f"O arquivo {self.arquivo} não foi encontrado.")
        return conteudo

    def extrair_linha(self, numero_linha: int):
        if 1 <= numero_linha <= len(self.conteudo):
            return self.conteudo[numero_linha - 1].strip()
        else:
            return f"Linha {numero_linha} não existe no arquivo."

musica = ArquivoTexto("musica.txt")
print(musica.conteudo)
print(musica.extrair_linha(2))



# 6.2 Classe para ler arquivos de csv
# Crie a classe `ArquivoCSV`. Ela deve extender (herdar) a classe ArquivoTexto para reaproveitar os seus atributos (self.arquivo e self.conteudo). Além disso, adicione o seguinte atributo:
# self.colunas: Atributo do tipo `list` onde os elementos são os nome das colunas;
# A classe também deve conter o seguinte método:
# self.extrair_nome_colunas: Método que retorna o nome das colunas do arquivo.
# extrair_coluna: Método que recebe como parâmetro o indice da coluna e retorna o valor em questão. Considere a primeira coluna como número 1.
# Veja abaixo a estrutura do arquivo csv:
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


import sys
sys.path.insert(0, '/data')
from arquivo_texto import ArquivoTexto

class ArquivoCSV(ArquivoTexto):
    def __init__(self, arquivo: str):
        super().__init__(arquivo=arquivo)
        self.colunas = []
        self._extrair_colunas()

    def _extrair_colunas(self):
        """Método auxiliar para extrair as colunas do cabeçalho do CSV"""
        primeira_linha = self.conteudo[0]
        self.colunas = primeira_linha.strip().split(',')

    def extrair_nome_colunas(self):
        """Método que retorna os nomes das colunas"""
        return self.colunas

    def extrair_coluna(self, indice_coluna: int):
        """Método que recebe o índice da coluna (1-based) e retorna a coluna inteira"""
        if indice_coluna < 1 or indice_coluna > len(self.colunas):
            raise IndexError("Índice de coluna fora do intervalo")
        coluna = []
        for linha in self.conteudo[1:]:
            colunas_linha = linha.strip().split(',')
            coluna.append(colunas_linha[indice_coluna - 1])
        return coluna



