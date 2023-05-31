import random

from jogador import Jogador
#A classe AgenteComputadorAleatorio é uma subclasse da classe Jogador
class AgenteComputadorAleatorio(Jogador):
    def __init__(self, letra):
        super().__init__(letra)  # Chama o construtor da classe pai (Jogador) para inicializar a letra do jogador

    def retornar_jogada(self, jogo):
        posicao = random.choice(jogo.movimentos_disponiveis())  # Escolhe uma posição aleatória entre as posições disponíveis no jogo
        return posicao