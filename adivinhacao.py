import random

#Definição da função
import funcoes


def jogar():
    jogo = 'Advinhação'
    funcoes.bem_vindo(jogo)

    numero_secreto = random.randrange(1,101)
    print(numero_secreto)
    total_de_tentativas = 0
    pontos = 1000

    funcoes.mensagem_nivel_dificuldade()
    nivel = funcoes.input_inteiro('Defina o nível: ')
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        funcoes.mostrador_tentativas(rodada, total_de_tentativas)
        chute = funcoes.input_inteiro('Digite um número entre 1 e 100: ')
        print(f'Você digitou {chute}')

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue    # Continue irá para a próxima iteração até digitar o resultado desejado

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            funcoes.mensagem_ganhador(pontos)
            break   # Break irá parar a iteração
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")


# Função de modularização do código, faz com que o código só seja ativado ao ativar como main
if(__name__ == "__main__"):
    jogar()
