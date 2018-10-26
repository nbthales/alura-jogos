from random import randint


def jogar():

    print('*' * 33)
    print('Bem vindo ao jogo de Adivinhação!')
    print('*' * 33)

    numero_secreto = randint(1, 100)
    total_de_tentativas = 0
    pontos = 1000
    #rodada = 1

    print('Qual nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')
    nivel = int(input('Define o nível: '))

    if nivel == 1:
        total_de_tentativas = 20

    elif nivel == 2:
        total_de_tentativas = 10

    else:
        total_de_tentativas = 5

    #while rodada <= total_de_tentativas:
    for rodada in range(1, total_de_tentativas +1):
        print(f'Tentativa {rodada} de {total_de_tentativas}.')
        chute = int(input('Digite um número entre 1 e 100: '))
        if chute < 1 or chute > 100:
            print('Você deve digitar um número entre 1 e 100!')
            continue
        if numero_secreto == chute:
            print(f'Você acertou e fez {pontos} pontos!')
            break
        else:
            if chute > numero_secreto:
                print('Você errou! O seu chute foi maior do que o número secreto.')
            elif chute < numero_secreto:
                print('Você errou! O seu chute foi menor que o número secreto.')
        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos
        #rodada += 1
    print('Fim do Jogo')


if __name__ == '__main__':
    jogar()
