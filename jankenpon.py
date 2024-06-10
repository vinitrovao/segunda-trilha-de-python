# flake8: noqa
import random


def obter_escolha_do_computador():
    escolhas = ['pedra', 'papel', 'tesoura']
    return random.choice(escolhas)


def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return 'empate'
    elif (jogador == 'pedra' and computador == 'tesoura') or \
         (jogador == 'papel' and computador == 'pedra') or \
         (jogador == 'tesoura' and computador == 'papel'):
        return 'jogador'
    else:
        return 'computador'


def jogar():
    vitorias_jogador = 0
    vitorias_computador = 0
    rodadas_necessarias_para_vencer = 5

    while vitorias_jogador < rodadas_necessarias_para_vencer and vitorias_computador < rodadas_necessarias_para_vencer: 

        escolha_do_jogador = input("Escolha pedra, papel ou tesoura: ").lower()
        
        if escolha_do_jogador not in ['pedra', 'papel', 'tesoura']:
            print("Escolha inválida, tente novamente.")
            continue
        
        escolha_do_computador = obter_escolha_do_computador()
        print(f"O computador escolheu: {escolha_do_computador}")

        resultado = determinar_vencedor(escolha_do_jogador, escolha_do_computador) 

        
        if resultado == 'jogador':
            vitorias_jogador += 1
            print("Você ganhou esta rodada!")
        elif resultado == 'computador':
            vitorias_computador += 1
            print("O computador ganhou esta rodada!")
        else:
            print("Esta rodada foi um empate!")
        
        print(f'Placar: Jogador {vitorias_jogador} - {vitorias_computador} Computador')

    if vitorias_jogador == rodadas_necessarias_para_vencer:
        print("Parabéns! Você ganhou o jogo!")
    else:
        print("O computador ganhou o jogo! Tente novamente.")


if __name__ == "__main__":
    jogar()
