import random

from jogador import Jogador
#A classe AgenteComputadorAleatorio é uma subclasse da classe Jogador
class AgenteComputadorAleatorio(Jogador):
    def __init__(self, letra):
        # Chama o construtor da classe pai (Jogador) para inicializar a letra do jogador
        super().__init__(letra)

    def retornar_jogada(self, jogo):
        # Escolhe uma posição aleatória entre as posições disponíveis no jogo
        posicao = random.choice(jogo.movimentos_disponiveis())
        return posicao