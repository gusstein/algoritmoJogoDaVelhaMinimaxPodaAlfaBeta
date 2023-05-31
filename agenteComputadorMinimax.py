import random
import math

from jogador import Jogador
#A classe AgenteComputadorMinimax é uma subclasse da classe Jogador
class AgenteComputadorMinimax(Jogador):
    #O método __init__ é o construtor da classe
    # Ele recebe a letra do jogador X ou O
    # O construtor chama o construtor da classe pai (Jogador) e
    # inicializa o atributo max_profundidade com o valor inteiro obtido a partir da entrada do usuário
    def __init__(self, letra):
        super().__init__(letra)
        print("-----------------------------------------")
        self.max_profundidade = int(input("Defina a profundidade máxima da busca para |" + letra + "|"
           "\n -|"))
        print("-----------------------------------------")

    #O método retornar_jogada recebe um objeto jogo como parâmetro e retorna a próxima jogada a partir do minimax ou aleatória
    def retornar_jogada(self, jogo):
        # Se for a primeira jogada vai aleatório
        if len(jogo.movimentos_disponiveis()) == 16:
            nova_posicao = random.choice(jogo.movimentos_disponiveis())
        else:
            nova_posicao = self.minimax(jogo, self.letra, self.max_profundidade)['posicao']
        return nova_posicao

    def minimax(self, jogo, jogador, profundidade):
        # Obtém a letra do jogador atual
        jogador_max = self.letra
        # Define a letra do outro jogador com base na letra do jogador atual
        outro_jogador = 'O' if jogador == 'X' else 'X'

        # Verifica se o outro jogador é o vencedor do estado atual do jogo
        # Retorna um dicionário com a posição como None e a pontuação calculada
        #
        # A pontuação é determinada pelo número
        # de posicoes vazias multiplicado por 1 se o outro jogador for o jogador max, ou multiplicado por -1 se for o jogador min
        if jogo.vencedor_atual == outro_jogador:
            return {'posicao': None,'pontuacao': 1 * (jogo.num_posicoes_vazias() + 1) if outro_jogador == jogador_max
                        else -1 * (jogo.num_posicoes_vazias() + 1)}
        elif not jogo.posicoes_vazias() or profundidade == 0:
            #Retorna um dicionário com a posição como None e a pontuação obtida através da função heuristica
            return {'posicao': None, 'pontuacao': self.heuristica_vencedor_jogo(jogo, jogador_max)}


        #Verifica se o jogador atual é o jogador max
        if jogador == jogador_max:
            # Inicializa a melhor jogada como tendo uma pontuação inicial de menos infinito
            melhor_jogada = {'posicao': None, 'pontuacao': -math.inf}
            # Caso contrário, inicializa a melhor jogada com uma pontuação de mais infinito
        else:
            melhor_jogada = {'posicao': None, 'pontuacao': math.inf}

        #Itera sobre todas as jogadas possíveis no estado atual
        for jogada_possivel in jogo.movimentos_disponiveis():
            #Faz uma jogada possível no estado atual
            jogo.fazer_jogada(jogada_possivel, jogador)
            #Chama recursivamente a função minimax para o próximo estado
            #com o outro jogador como jogador atual e uma profundidade reduzida em 1
            sim_pontuacao = self.minimax(jogo, outro_jogador, profundidade - 1)
            # Desfaz a jogada feita no jogo atual
            jogo.tabuleiro[jogada_possivel] = ' '
            # Reseta o vencedor atual do jogo
            jogo.vencedor_atual = None
            #Define a posição da jogada atual no dicionário sim_pontuacao.
            sim_pontuacao['posicao'] = jogada_possivel

            # Verifica se o jogador atual é o jogador max
            if jogador == jogador_max:
                #Verifica se a pontuação da jogada atual é maior que a pontuação da melhor jogada encontrada
                if sim_pontuacao['pontuacao'] > melhor_jogada['pontuacao']:
                    melhor_jogada = sim_pontuacao
            else:
                #verifica se a pontuação da jogada atual é menor que a pontuação da melhor jogada encontrada
                if sim_pontuacao['pontuacao'] < melhor_jogada['pontuacao']:
                    melhor_jogada = sim_pontuacao

        # melhor_jogada, que contém a posição e a pontuação da melhor jogadas
        return melhor_jogada

    def heuristica_vencedor_jogo(self, jogo, jogador_max):
        outro_jogador = 'O' if jogador_max == 'X' else 'X'
        # Verifica se o jogador atual é o vencedor
        if jogo.vencedor_atual == jogador_max:
            return 1
        # Verifica se o outro jogador é o vencedor3
        elif jogo.vencedor_atual == outro_jogador:
            return -1
        # Caso contrário, o jogo está empatado
        else:
            return 0

