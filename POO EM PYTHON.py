import random

def escolha_computador():
    escolhas = ['pedra', 'papel', 'tesoura']
    return random.choice(escolhas)

def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return 'Empate!'
    elif (jogador == 'pedra' and computador == 'tesoura') or \
         (jogador == 'papel' and computador == 'pedra') or \
         (jogador == 'tesoura' and computador == 'papel'):
        return 'Você venceu!'
    else:
        return 'Computador venceu!'

def jogo():
    jogador = input("Escolha pedra, papel ou tesoura: ").lower()
    while jogador not in ['pedra', 'papel', 'tesoura']:
        jogador = input("Escolha inválida. Escolha pedra, papel ou tesoura: ").lower()

    computador = escolha_computador()
    print(f"Computador escolheu: {computador}")

    resultado = determinar_vencedor(jogador, computador)
    print(resultado)

if __name__ == "__main__":
    jogo()
