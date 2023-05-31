import time

from agenteHumano import AgenteHumano
from jogoDaVelha import JogoDaVelha
from agenteComputadorMinimax import AgenteComputadorMinimax
from agenteComputadorAleatorio import AgenteComputadorAleatorio

from agenteComputadorMinimaxPodaAlfaBeta import AgenteComputadorMinimaxPodaAlfaBeta


# Controla todo o jogo
def jogar(jogo, jogador_x, jogador_o):
    jogo.imprimir_numeros_tabuleiro()
    # primeiro a jogar
    letra = 'X'
    num_jogadas = 0

    # Enquanto ainda há posicoes vazias no tabuleiro
    while jogo.posicoes_vazias():
        if letra == 'O':
            # Marca o início do tempo de jogada
            inicio_tempo = time.time()
            # Obtém a jogada do jogador O
            posicao = jogador_o.retornar_jogada(jogo)
            # Calcula o tempo de jogada
            tempo_jogada = time.time() - inicio_tempo
        else:
            #Marca o início do tempo de jogada
            inicio_tempo = time.time()
            #Obtém a jogada do jogador X
            posicao = jogador_x.retornar_jogada(jogo)
            # Calcula o tempo de jogada
            tempo_jogada = time.time() - inicio_tempo

        if jogo.fazer_jogada(posicao, letra):
            # Incrementa o número de jogadas
            num_jogadas += 1
            print("--------------------------------------------")
            print("|JOGADOR "+letra+ "|")
            print("Jogada " + num_jogadas.__str__() + ":")
            print("Tempo da jogada: " + tempo_jogada.__str__()  + " segundos")
            jogo.imprimir_tabuleiro()
            print('')

            # Se houver um vencedor
            if jogo.vencedor_atual:

                print(letra + ' vence!')
                return letra
            # Alterna o jogador
            letra = 'O' if letra == 'X' else 'X'
        time.sleep(.8)

    print('Jogo empatado')

#Menu inicial
if __name__ == '__main__':
    while True:
        modo_jogo = input("Game mode - [ 1 - Humano X Computador || 2 - Computador X Computador ]"
                " \n -| ")

        jogador_x = None
        jogador_o = None
        #Defiição de modo e estratégia de jogo
        if modo_jogo == '1':
            jogador_x = AgenteHumano('X')

            estrategia_jogador_o = input(
                "Estratégia |JOGADOR O| [ 1 - Aleatória || 2 - Minimax || 3 - Minimax com poda Alfa-beta ]"
                " \n -| ")

            if estrategia_jogador_o == '1':
                jogador_o = AgenteComputadorAleatorio('O')
            elif estrategia_jogador_o == '2':
                jogador_o = AgenteComputadorMinimax('O')
            elif estrategia_jogador_o == '3':
                jogador_o = AgenteComputadorMinimaxPodaAlfaBeta('O')

        elif modo_jogo == '2':
            estrategia_jogador_x = input(
                "Estratégia |JOGADOR X| [ 1 - Aleatória || 2 - Minimax || 3 - Minimax com poda Alfa-beta ]"
                " \n -| ")
            estrategia_jogador_o = input(
                "Estratégia |JOGADOR O| [ 1 - Aleatória || 2 - Minimax || 3 - Minimax com poda Alfa-beta ]"
                " \n -| ")

            if estrategia_jogador_x == '1':
                jogador_x = AgenteComputadorAleatorio('X')
            elif estrategia_jogador_x == '2':
                jogador_x = AgenteComputadorMinimax('X')
            elif estrategia_jogador_x == '3':
                jogador_x = AgenteComputadorMinimaxPodaAlfaBeta('X')

            if estrategia_jogador_o == '1':
                jogador_o = AgenteComputadorAleatorio('O')
            elif estrategia_jogador_o == '2':
                jogador_o = AgenteComputadorMinimax('O')
            elif estrategia_jogador_o == '3':
                jogador_o = AgenteComputadorMinimaxPodaAlfaBeta('O')

        else:
            print("Modo de jogo inválido.")
            exit()
        #Inicio de jogo - Verifica se os jogadores foram definidos corretamente
        if jogador_x is not None and jogador_o is not None:
            jogo = JogoDaVelha()
            jogar(jogo, jogador_x, jogador_o)
        else:
            print("Erro ao selecionar Jogador")

        novamente = input("Deseja continuar jogando [S/N]? "
                " \n -| ")
        if novamente.upper() == "N":
            break
