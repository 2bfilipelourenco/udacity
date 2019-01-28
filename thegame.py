from random import randint
from time import sleep

class Player:
    acoes_validas = ['pedra', 'papel', 'tesoura'] # Ações válidas para o jogador seja ele humano ou computador;

    def acao(self, minha_acao, acao_oponente):
        return minha_acao

class Aleatorio(Player):
    def acao(self, minha_acao, acao_oponente):
        return self.acoes_validas[randint(0, 2)] # Escolhe aleatoriamente uma opção de 0 a 2 equivalente as opções definidas na variável 'acoes_validas';
        
class Humano(Player):
    def acao(self, minha_acao, acao_oponente):
        acoes_jogador = input('Digite a sua jogada e aperte a tecla enter ~ Pedra, Papel ou Tesoura \n') # Recebe na variável 'acoes_jogador' a jogada escolhida pelo usuário.
        while acoes_jogador not in self.acoes_validas:
            acoes_jogador = input('\nJogada inválida. Tente digitar as palavras ~ Pedra, Papel ou Tesoura ~ para jogar.\n') # Caso a jogada não seja digitada corretamente, emitirá uma mensagem invalidando o input até que o mesmo esteja correto.
        return acoes_jogador

class Copiador(Player):
    def acao(self, minha_acao, acao_oponente):
        if acao_oponente == 'pedra': # O computador joga em relação ao input escolhido pelo adversário.
            return 'pedra'
        if acao_oponente == 'papel':
            return 'papel'
        else:
            return 'tesoura'

class Ciclo(Player):
    pass # Eu entendi a lógica, mas não estou conseguindo executar o código. Eu sei que tenho que dar um valor inicial para que a partir desse valor, eu consiga determinar a próxima jogada.

class Game: # Classe que possui as definições que darão ao usuário as informações/estatísticas do jogo.
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    def vencedor(self, e1_acao, e2_acao):
        if e1_acao == e2_acao:
            return '> > > Não houveram vencedores!\n', 0
        elif ((e1_acao == 'pedra' and e2_acao == 'tesoura') or
              (e1_acao == 'tesoura' and e2_acao == 'papel') or
              (e1_acao == 'papel' and e2_acao == 'pedra')):
            print('> > > O JOGADOR Nº 1 ganhou!\n')
            return 1
        else:
            print('> > > O JOGADOR Nº 2 ganhou!\n')
            return 2

    def placar(self, ganhador_partida, e1_placar_anterior, e2_placar_anterior):
        if ganhador_partida == 1:
            e1_novo_placar = e1_placar_anterior + 1
            print(f'O Placar do JOGADOR Nº 1 é [{e1_novo_placar}] e o placar do JOGADOR Nº 2 é [{e2_placar_anterior}].\n')
            return e1_novo_placar, e2_placar_anterior
        elif ganhador_partida == 2:
            e2_novo_placar = e2_placar_anterior + 1
            print(f'O Placar do JOGADOR Nº 1 é [{e1_placar_anterior}] e o placar do JOGADOR Nº 2 é [{e2_novo_placar}].\n')
            return e1_placar_anterior, e2_novo_placar
        else:
            print(f'O Placar do JOGADOR Nº 1 é [{e1_placar_anterior}] e o placar do JOGADOR Nº 2 é [{e2_placar_anterior}].\n')
            return e1_placar_anterior, e2_placar_anterior

    def placar_final(self, e1_pontuacao, e2_pontuacao):
        print(f'\nO placar final ficou em [{e1_pontuacao}] X [{e2_pontuacao}].')
        if e1_pontuacao > e2_pontuacao:
            print('> > > Parabéns JOGADOR Nº 1!')
        elif e1_pontuacao < e2_pontuacao:
            print('> > > Parabéns JOGADOR Nº 2!')
        else:
            print('> > > O jogo ficou EMPATADO!')

    def play_round(self, partida_atual, partida_final, e1_acao_anterior, e2_acao_anterior):
        if partida_atual == 1:
           e1_acao = self.e1.acao('tesoura', 'pedra')
           e2_acao = self.e2.acao('tesoura', 'pedra')
           print(f'\nO JOGADOR Nº 1 escolheu {e1_acao} e o JOGADOR Nº 2 escolheu {e2_acao}.')
           return e1_acao, e2_acao
        else:
            e1_acao = self.e1.acao(e1_acao_anterior, e2_acao_anterior)
            e2_acao = self.e2.acao(e1_acao_anterior, e2_acao_anterior)
            print(f'\nO JOGADOR Nº 1 escolheu {e1_acao} e o JOGADOR Nº 2 escolheu {e2_acao}.')
            return e1_acao, e2_acao

    def play_match(self):
        partidas = int(input('\nQuantas partidas você vai querer jogar? '))
        input('\nQue o jogo comece!\n' + '> > > Aperte a tecla enter para continuar.')
        e1_pontuacao, e2_pontuacao = 0, 0
        e1_acao_anterior = 'tesoura'
        e2_acao_anterior = 'papel'
        
        for round in range(1, partidas+1):
                print(f'\nPARTIDA DE Nº {round}')
                e1_acao, e2_acao = self.play_round(round, partidas, e1_acao_anterior, e2_acao_anterior)
                vencedor_partida = self.vencedor(e1_acao, e2_acao)
                e1_pontuacao, e2_pontuacao = self.placar(vencedor_partida, e1_pontuacao, e2_pontuacao)

        self.placar_final(e1_pontuacao, e2_pontuacao)
        sleep(15)

if __name__ == '__main__':
    print('Aleatorio ~ Humano ~ Copiador ~ Ciclo\n')
    jogadores = {'Aleatorio': Aleatorio(), 'Humano': Humano(), 'Copiador': Copiador(), 'Ciclo': Ciclo()}
    j1 = input('Digite a opção que será o jogador Nº 1?! ')
    j2 = input('Digite a opção que será o jogador Nº 2?! ')
    game = Game(jogadores[j1], jogadores[j2])
    game.play_match()
