from jogador import Jogador

class AgenteHumano(Jogador):
    # construtor da classe e recebe um parâmetro letra, que representa a letra ('X' ou 'O')
    # do jogador. Esse método chama o construtor da superclasse (Jogador) passando a letra como argumento
    def __init__(self, letra):
        super().__init__(letra)

    #obter_jogada é responsável por obter a jogada do jogador humano.
    # Ele recebe como parâmetro o objeto jogo, que representa o estado atual do jogo
    def retornar_jogada(self, jogo):
        quadrado_valido = False
        valor = None
        while not quadrado_valido:
            quadrado = input('Vez do jogador ' + self.letra + '. Insira a jogada (0-15): ')
            try:
                valor = int(quadrado)
                #vrifica se o valor está presente na lista de movimentos disponíveis no objeto jogo
                # (retornada pelo método movimentos_disponiveis())
                if valor not in jogo.movimentos_disponiveis():
                    raise ValueError
                quadrado_valido = True
            except ValueError:
                print('Quadrado inválido. Tente novamente.')
        #jogada do jogador
        return valor