import random
import math

from jogador import Jogador


#A classe AgenteComputadorMinimaxPodaAlfaBeta é uma subclasse da classe Jogador
class AgenteComputadorMinimaxPodaAlfaBeta(Jogador):
    #É o método construtor da classe que recebe um parâmetro letra que representa a letra do jogador ('X' ou 'O')
    # Ele chama o construtor da classe pai Jogador e inicializa a
    # variável max_profundidade com um valor fornecido pelo usuário
    def __init__(self, letra):
        super().__init__(letra)
        # Define a profundidade máxima da busca
        print("-----------------------------------------")
        self.max_profundidade = int(input("Defina a profundidade máxima da busca para |" + letra + "|"
           "\n -|"))
        print("-----------------------------------------")

    # Este método é responsável por obter a próxima jogada do agente de computador
    # Ele recebe como parâmetro um objeto jogo da classe
    def retornar_jogada(self, jogo):
        if len(jogo.movimentos_disponiveis()) == 16:
            quadrado = random.choice(jogo.movimentos_disponiveis())
        else:
            quadrado = self.minimaxPodaAlfaBeta(jogo, self.letra, self.max_profundidade, -math.inf, math.inf)['posicao']
        return quadrado

    # Ele recebe como parâmetros o estado atual do jogo, o jogador atual, a profundidade atual na árvore de jogadas
    # o valor de alfa (o melhor valor máximo encontrado até o momento) e
    # o valor de beta (o melhor valor mínimo encontrado até o momento)
    def minimaxPodaAlfaBeta(self, estado, jogador, profundidade, alfa, beta):
        jogador_max = self.letra  # você mesmo
        outro_jogador = 'O' if jogador == 'X' else 'X'

        # #Verifica se o jogador atual é o vencedor,
        if estado.vencedor_atual == outro_jogador:
            #retorna um dicionário com a posição e a pontuação correspondente
            return {'posicao': None, 'pontuacao': 1 * (estado.num_quadrados_vazios() + 1) if outro_jogador == jogador_max else -1 * (
                    estado.num_quadrados_vazios() + 1)}
        # verifica se não há mais quadrados vazios ou se a profundidade máxima foi atingida
        elif not estado.quadrados_vazios() or profundidade == 0:
            # retorna um dicionário com a posição como nula e a pontuação obtida a partir da avaliação heurística do estado
            return {'posicao': None, 'pontuacao': self.heuristica_avaliar_estado(estado, jogador_max)}

        if jogador == jogador_max:
            # Maximixa pontuacao
            melhor_jogada = {'posicao': None, 'pontuacao': -math.inf}
        else:
            #Minimiza pontuação
            melhor_jogada = {'posicao': None, 'pontuacao': math.inf}

        #percorre todas as jogadas possíveis a partir do estado atual e
        # chama recursivamente o método minimaxPodaAlfaBeta para cada uma dessas jogadas
        # Ele alterna entre maximizar e minimizar a pontuação, dependendo do jogador atual
        for jogada_possivel in estado.movimentos_disponiveis():
            estado.fazer_jogada(jogada_possivel, jogador)
            # diminui a profundidade em cada chamada recursiva
            sim_pontuacao = self.minimaxPodaAlfaBeta(estado, outro_jogador, profundidade - 1, alfa, beta)

            # desfaz a jogada
            estado.tabuleiro[jogada_possivel] = ' '
            estado.vencedor_atual = None
            sim_pontuacao['posicao'] = jogada_possivel  # isso representa a jogada ótima seguinte

            # atualiza os valores de alfa e beta e realiza a poda quando beta for menor ou igual a alfa
            # Isso permite evitar a exploração de caminhos que não levarão a uma jogada ótima
            if jogador == jogador_max:  # X é o jogador máximo
                if sim_pontuacao['pontuacao'] > melhor_jogada['pontuacao']:
                    melhor_jogada = sim_pontuacao
                alfa = max(alfa, melhor_jogada['pontuacao'])
            else:
                if sim_pontuacao['pontuacao'] < melhor_jogada['pontuacao']:
                    melhor_jogada = sim_pontuacao
                beta = min(beta, melhor_jogada['pontuacao'])

                if beta <= alfa:
                    break

        #Retorna a melhor jogada encontrada, que é representada por um dicionário com as chaves 'posicao'
        # (a posição no tabuleiro onde a jogada deve ser feita) e 'pontuacao' (a pontuação atribuída à jogada)
        return melhor_jogada

    #Avalia o estado atual do jogo e retornar uma pontuação heurística
    def heuristica_avaliar_estado(self, estado, jogador):
        outro_jogador = 'O' if jogador == 'X' else 'X'
        # Verifica se o jogador atual é o vencedor
        if estado.vencedor_atual == jogador:
            return 1
        # Verifica se o outro jogador é o vencedor
        elif estado.vencedor_atual == outro_jogador:
            return -1
        # Caso contrário, o jogo está empatado
        else:
            return 0




