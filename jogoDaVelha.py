class JogoDaVelha():
    #O método __init__ é o construtor da classe, que inicializa o tabuleiro e o vencedor atual como None
    def __init__(self):
        self.tabuleiro = self.criar_tabuleiro()
        self.vencedor_atual = None

    # cria um novo tabuleiro vazio, representado por uma lista de 16 elementos
    # onde cada elemento inicialmente é um espaço em branco (' ')
    @staticmethod
    def criar_tabuleiro():
        return [' ' for _ in range(16)]

    #imprime o tabuleiro atual na saída, exibindo as linhas e colunas do jogo da velha
    def imprimir_tabuleiro(self):
        #cria uma lista contendo as linhas do tabuleiro, onde i varia de 0 a 3
        #dentro do loop cada linha é impressa no formato de um tabuleiro,
        # com os elementos separados por barras verticais (|). A expressão ' | '.join(row)
        # concatena os elementos de cada linha usando o separador ' | '
        for linha in [self.tabuleiro[i*4:(i+1) * 4] for i in range(4)]:
            print('| ' + ' | '.join(linha) + ' |')

    @staticmethod
    def imprimir_numeros_tabuleiro():
        numeros_tabuleiro = [['0', '1', '2', '3'], ['4', '5', '6', '7'], ['8', '9', '10', '11'], ['12', '13', '14', '15']]
        for linha in numeros_tabuleiro:
            print('| ' + ' | '.join(linha) + ' |')

    def fazer_jogada(self, posicao, letra):
        #verifica se a posicao escolhido está vazio
        if self.tabuleiro[posicao] == ' ':
            #a letra é colocada na posicao e é verificado se essa jogada resultou em uma vitória
            self.tabuleiro[posicao] = letra
            if self.verificar_vencedor(posicao, letra):
                self.vencedor_atual = letra
        #O método retorna True se a jogada foi feita com sucesso e False caso contrário
            return True
        return False

        #Verifica se alguma linhas em todas as direções foi traçada
    def verificar_vencedor(self, posicao, letra):
        # Índice da linha
        indice_linha = posicao // 4

        # Obtém a linha correspondente
        row = self.tabuleiro[indice_linha * 4: (indice_linha + 1) * 4]
        # Verifica se todas as posições da linha são iguais à letra do jogador atual
        if all([s == letra for s in row]):
            return True

        col_ind = posicao % 4  # Índice da coluna
        # Obtém a coluna correspondente
        column = [self.tabuleiro[col_ind + i * 4] for i in range(4)]
        # Verifica se todas as posições da coluna são iguais à letra do jogador atual
        if all([s == letra for s in column]):
            return True

        # Diagonal1
        if posicao % 5 == 0:
            # Obtém a diagonal principal
            diagonal1 = [self.tabuleiro[i] for i in [0, 5, 10, 15]]
            # Verifica se todas as posições da diagonal principal são iguais à letra do jogador atual
            if all([s == letra for s in diagonal1]):
                return True
        # Diagonal2
        if posicao in [3, 6, 9, 12]:
            # Obtém a diagonal secundária
            diagonal2 = [self.tabuleiro[i] for i in [3, 6, 9, 12]]
            # Verifica se todas as posições da diagonal secundária são iguais à letra do jogador atual
            if all([s == letra for s in diagonal2]):
                return True

        return False  # Não há vitória

    # Posicoes vazias no tabuleiro
    def posicoes_vazias(self):
        return ' ' in self.tabuleiro

    #Número de posicoes vazias
    def num_posicoes_vazias(self):
        return self.tabuleiro.count(' ')

    # Lista com os índices das posicoes vazias
    def movimentos_disponiveis(self):
        return [i for i, x in enumerate(self.tabuleiro) if x == " "]
