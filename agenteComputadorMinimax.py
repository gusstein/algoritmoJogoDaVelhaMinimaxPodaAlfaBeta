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

    # faz chamadas recursivas para avaliar os estados futuros do jogo
    def minimax(self, jogo, jogador, profundidade):
        # Obtém a letra do jogador atual
        jogador_max = self.letra
        # Define a letra do outro jogador com base na letra do jogador atual
        outro_jogador = 'O' if jogador == 'X' else 'X'

        #Verificar se o jogador atual perdeu o jogo.
        if jogo.vencedor_atual == outro_jogador:
            return {'posicao': None,'pontuacao': self.heuristica_vencedor_jogo(jogo, jogador_max)}
        #Verificar se o jogo chegou ao fim ou se a profundidade máxima foi alcançada
        elif not jogo.posicoes_vazias() or profundidade == 0:
            #Retorna um dicionário com a posição como None e a pontuação obtida através da função heuristica
            return {'posicao': None, 'pontuacao': self.heuristica_vencedor_jogo(jogo, jogador_max)}

        if jogador == jogador_max:
            # Maximixa pontuacao
            #Garante que uma jogada com uma pontuação mais alta seja selecionada.
            melhor_jogada = {'posicao': None, 'pontuacao': -math.inf}
        else:
            #Minimiza pontuação
            #Garate que uma jogada com uma pontuação mais baixa seja selecionada.
            melhor_jogada = {'posicao': None, 'pontuacao': math.inf}

        #Itera sobre todas as jogadas possíveis no estado atual
        for jogada_possivel in jogo.movimentos_disponiveis():
            jogo.fazer_jogada(jogada_possivel, jogador)
            pontuacao = self.minimax(jogo, outro_jogador, profundidade - 1)

            # Desfaz a jogada feita no jogo atual
            jogo.tabuleiro[jogada_possivel] = ' '
            # Reseta o vencedor atual do jogo
            jogo.vencedor_atual = None
            #Define a posição da jogada atual no dicionário pontuacao.
            pontuacao['posicao'] = jogada_possivel

            # Verifica se o jogador atual é o jogador max
            if jogador == jogador_max:
                #Verifica se a pontuação da jogada atual é maior que a pontuação da melhor jogada encontrada
                if pontuacao['pontuacao'] > melhor_jogada['pontuacao']:
                    melhor_jogada = pontuacao
            else:
                #verifica se a pontuação da jogada atual é menor que a pontuação da melhor jogada encontrada
                if pontuacao['pontuacao'] < melhor_jogada['pontuacao']:
                    melhor_jogada = pontuacao

        return melhor_jogada

    #A função heuristica_vencedor_jogo retorna uma
    # pontuação que representa a avaliação do estado do jogo para o max
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

