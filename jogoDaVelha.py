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
        for row in [self.tabuleiro[i*4:(i+1) * 4] for i in range(4)]:
            print('| ' + ' | '.join(row) + ' |')

    # imprime os números correspondentes aos quadrados do tabuleiro
    # para ajudar o jogador a escolher uma posição para jogar
    @staticmethod
    def imprimir_numeros_tabuleiro():
        numeros_tabuleiro = [[str(i) for i in range(j*4, (j+1)*4)] for j in range(4)]
        for row in numeros_tabuleiro:
            print('| ' + ' | '.join(row) + ' |')

    def fazer_jogada(self, quadrado, letra):
        #verifica se o quadrado escolhido está vazio
        if self.tabuleiro[quadrado] == ' ':
            #a letra é colocada no quadrado e é verificado se essa jogada resultou em uma vitória
            self.tabuleiro[quadrado] = letra
            if self.verificar_vencedor(quadrado, letra):
                self.vencedor_atual = letra
        #O método retorna True se a jogada foi feita com sucesso e False caso contrário
            return True
        return False

    def verificar_vencedor(self, quadrado, letra):
        #Verifica se alguma linhas em todas as direções foi traçada
        row_ind = quadrado // 4  # Índice da linha
        # Obtém a linha correspondente
        row = self.tabuleiro[row_ind * 4: (row_ind + 1) * 4]
        # Verifica se todas as posições da linha são iguais à letra do jogador atual
        if all([s == letra for s in
                row]):
            return True

        col_ind = quadrado % 4  # Índice da coluna
        # Obtém a coluna correspondente
        column = [self.tabuleiro[col_ind + i * 4] for i in range(4)]
        # Verifica se todas as posições da coluna são iguais à letra do jogador atual
        if all([s == letra for s in
                column]):
            return True

        if quadrado % 5 == 0:  # Diagonal principal (0, 5, 10, 15)
            # Obtém a diagonal principal
            diagonal1 = [self.tabuleiro[i] for i in [0, 5, 10, 15]]
            # Verifica se todas as posições da diagonal principal são iguais à letra do jogador atual
            if all([s == letra for s in
                    diagonal1]):
                return True

        if quadrado in [3, 6, 9, 12]:  # Diagonal secundária (3, 6, 9, 12)
            # Obtém a diagonal secundária
            diagonal2 = [self.tabuleiro[i] for i in [3, 6, 9, 12]]
            # Verifica se todas as posições da diagonal secundária são iguais à letra do jogador atual
            if all([s == letra for s in
                    diagonal2]):
                return True

        return False  # Não há vitória

    # Quadrados vazios no tabuleiro
    def quadrados_vazios(self):
        return ' ' in self.tabuleiro

    #Número de quadrados vazios
    def num_quadrados_vazios(self):
        return self.tabuleiro.count(' ')

    # Lista com os índices dos quadrados vazios
    def movimentos_disponiveis(self):
        return [i for i, x in enumerate(self.tabuleiro) if x == " "]
