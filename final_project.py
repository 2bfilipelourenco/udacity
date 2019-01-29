from random import randint
from time import sleep

class Player():
    acoes_validas = ['pedra', 'papel', 'tesoura']

    def __init__(self):
        self.placar = 0
        self.my_move = None
        self.last_opponent_move = None

    def play(self):
        return 'pedra'

    def learn(self, my_move): # Se eu colocar o 'last_oponnent_move' aqui, o aplicativo dá 'crash'.
        self.my_move = my_move

class RandomPlayer(Player):
    def play(self):
        return self.acoes_validas[randint(0, 2)]

class HumanPlayer(Player):
    def play(self):
        player_move = input(' Digite sua jogada utilizando apenas letras minúsculas: pedra, papel ou tesoura!\n ')
        while player_move not in self.acoes_validas:
            player_move = input(' Jogada digitada inválida. Tente digitar uma dessas jogadas: pedra, papel ou tesoura!\n ')
        return player_move

class CyclePlayer(Player):
    def play(self):
        if self.my_move == None:
            return 'pedra'
        elif self.my_move == 'pedra':
            return 'papel'
        elif self.my_move == 'papel':
            return 'tesoura'
        else:
            return 'pedra'

class ReflectPlayer(Player):
    def play(self):
        if self.last_opponent_move is None:
            return Player.play(self)
        return self.last_opponent_move

    def learn(self, last_opponent_move):
        self.last_opponent_move = last_opponent_move
        
class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    
    def play_match(self):
        print('\n PEDRA, PAPEL ou TESOURA ~ O jogo começou!')
        rounds = int(input(' > > > Digite o número de partidas que você quer jogar:\n '))
        
        for partida in range(0, rounds):
            print(f'\n \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')
            print(f" \/\/\/\/\/\/ PARTIDA DE Nº: {partida} \/\/\/\/\/\/")
            self.play_round()

        if self.player1.placar > self.player2.placar:
            print('\n Parabéns! O jogador Nº1 ganhou o jogo.')
            print(f' ************************************************************************************')
        elif self.player1.placar > self.player2.placar:
            print('\n Parabéns! O jogador Nº2 ganhou o jogo.!')
            print(f' ************************************************************************************')
        else:
            print('\n Ops! O jogo ficou empatado ... ;) ...')
            print(f' ************************************************************************************')

        print(f'\n O placar final do jogo ficou em: {self.player1.placar} --||-- {self.player2.placar}')
        print(" > > > O jogo acabou! Essa janela será fechada em 15 segundos.")
        sleep(15)

    def play_round(self):
        player1_jogada = self.player1.play()
        player2_jogada = self.player2.play()

        self.player1.learn(player2_jogada)
        self.player2.learn(player1_jogada)

        if ((player1_jogada == 'pedra' and player2_jogada == 'tesoura') or
            (player1_jogada == 'tesoura' and player2_jogada == 'papel') or
            (player1_jogada == 'papel' and player2_jogada == 'pedra')):
            self.player1.placar += 1
            print(f' ____________________________________________________________________________________')
            print('\n Jogador Nº 1 ganhou a partida!')
            print(f' O placar do jogo está: {self.player1.placar} --||-- {self.player2.placar}')
            print(f' O jogador Nº1 jogou "{player1_jogada}" e o jogador Nº2 jogou "{player2_jogada}".')

        elif ((player2_jogada == 'pedra' and player1_jogada == 'tesoura') or
              (player2_jogada == 'tesoura' and player1_jogada == 'papel') or
              (player2_jogada == 'papel' and player1_jogada == 'pedra')):
            self.player2.placar += 1
            print(f' ____________________________________________________________________________________')
            print('\n Jogador Nº 2 ganhou a partida!')
            print(f' O placar do jogo está: {self.player1.placar} --||-- {self.player2.placar}')
            print(f' O jogador Nº1 jogou "{player1_jogada}" e o jogador Nº2 jogou "{player2_jogada}".')

        else:
            print(f' ____________________________________________________________________________________')
            print('\n A partida está empatada!')
            print(f' O placar do jogo está: {self.player1.placar} --||-- {self.player2.placar}')
            print(f' Ambos fizeram a mesma jogada. O jogador Nº1 jogou "{player1_jogada}" e o jogador Nº2 jogou "{player2_jogada}".')

game = Game(RandomPlayer(), HumanPlayer())
game.play_match()

#chamada_escolhas = ' [1]RandomPlayer, [2]HumanPlayer, [3]ReflectPlayer, [4]CyclePlayer'

#if __name__ == '__main__':
    #jogadores_disponiveis = {1: RandomPlayer(), 2: HumanPlayer(), 3: ReflectPlayer(), 4: CyclePlayer()}
    #print (chamada_escolhas)
    #print(f' ************************************************************************************\n')

    #e1 = input(" Digite o número correspondente ao jogador Nº1: ")
    #e2 = input(" Digite o número correspondente ao jogador Nº2: ")

    #game = Game(jogadores_disponiveis[e1], jogadores_disponiveis[e2])
    #game.play_match()
