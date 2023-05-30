import time

from agenteHumano import AgenteHumano
from jogoDaVelha import JogoDaVelha
from agenteComputadorMinimax import AgenteComputadorMinimax
from agenteComputadorAleatorio import AgenteComputadorAleatorio

from agenteComputadorMinimaxPodaAlfaBeta import AgenteComputadorMinimaxPodaAlfaBeta

def jogar(jogo, jogador_x, jogador_o, imprimir_jogo=True):
    # Controla todo o jogo
    if imprimir_jogo:
        jogo.imprimir_numeros_tabuleiro()  # Imprime os números das posições do tabuleiro
    letra = 'X'  # Define a letra do jogador atual como X

    num_jogadas = 0
    while jogo.quadrados_vazios():  # Enquanto ainda há quadrados vazios no tabuleiro
        tempo_jogada = 0
        if letra == 'O':
            inicio_tempo = time.time()  # Marca o início do tempo de jogada
            quadrado = jogador_o.retornar_jogada(jogo)  # Obtém a jogada do jogador O
            tempo_jogada = time.time() - inicio_tempo  # Calcula o tempo de jogada
        else:
            inicio_tempo = time.time()  # Marca o início do tempo de jogada
            quadrado = jogador_x.retornar_jogada(jogo)  # Obtém a jogada do jogador X
            tempo_jogada = time.time() - inicio_tempo  # Calcula o tempo de jogada
        if jogo.fazer_jogada(quadrado, letra):  # Faz a jogada no tabuleiro
            num_jogadas += 1  # Incrementa o número de jogadas
            if imprimir_jogo:
                print("--------------------------------------------")
                print(f"Jogada {num_jogadas}:")
                print(f"Tempo de jogada: {tempo_jogada:.2f} segundos")  # Imprime o tempo de jogada
                jogo.imprimir_tabuleiro()  # Imprime o tabuleiro atual
                print('')

            if jogo.vencedor_atual:  # Se houver um vencedor
                if imprimir_jogo:
                    print(letra + ' vence!')  # Imprime qual jogador venceu
                return letra  # Retorna a letra do jogador vencedor

            letra = 'O' if letra == 'X' else 'X'  # Alterna a letra do jogador atual

        time.sleep(.8)  # Aguarda um tempo antes da próxima jogada

    if imprimir_jogo:
        print('Empatou')  # Se não houver vencedor, imprime que o jogo empatou

#Menu inicial
if __name__ == '__main__':
    while True:
        modo_jogo = input("Selecione o modo de jogo [ 1 - Humano X Computador || 2 - Computador X Computador ]"
                " \n -| ")

        jogador_x = None
        jogador_o = None
        #Defiição de modo e estratégia de jogo
        if modo_jogo == '1':
            jogador_x = AgenteHumano('X')

            estrategia_jogador_o = input(
                "Selecione a estratégia para o |JOGADOR O| [ 1 - Aleatória || 2 - Minimax || 3 - Minimax com poda Alfa-beta ]"
                " \n -| ")

            if estrategia_jogador_o == '1':
                jogador_o = AgenteComputadorAleatorio('O')
            elif estrategia_jogador_o == '2':
                jogador_o = AgenteComputadorMinimax('O')
            elif estrategia_jogador_o == '3':
                jogador_o = AgenteComputadorMinimaxPodaAlfaBeta('O')

        elif modo_jogo == '2':
            estrategia_jogador_x = input(
                "Selecione a estratégia para o |JOGADOR X| [ 1 - Aleatória || 2 - Minimax || 3 - Minimax com poda Alfa-beta ]"
                " \n -| ")
            estrategia_jogador_o = input(
                "Selecione a estratégia para o |JOGADOR O| [ 1 - Aleatória || 2 - Minimax || 3 - Minimax com poda Alfa-beta ]"
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
            jogar(jogo, jogador_x, jogador_o, imprimir_jogo=True)
        else:
            print("Jogadores não definidos corretamente.")

        novamente = input("Deseja continuar jogando (S/N)? "
                " \n -| ")
        if novamente.upper() == "N":
            break
