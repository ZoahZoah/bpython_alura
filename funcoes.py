import random

def bem_vindo(jogo):
    print('*********************************')
    print(f'***Bem vindo ao jogo da {jogo}!***')
    print('*********************************')

def mensagem_ganhador():
    print('Parabéns, você ganhou!')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagem_perdedor(palavra_secreta):
    print('Puxa, você foi enforcado!')
    print(f'A palavra era {palavra_secreta}')
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def fim_jogo():
    print('Fim de jogo!!!')

def ler_txt():
    lista = []
    with open('palavras.txt') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            lista.append(linha)

    numero = random.randrange(0, len(lista))
    palavra_random = lista[numero].upper()
    return palavra_random

def inicializa_letras_acertadas(str, palavra_secreta):
    return [str for letra in palavra_secreta]

def solicita_chute():
    chute = input('Qual letra? ')
    # '.strip' remove os espaços declarados
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            print(index)
            letras_acertadas[index] = letra
        index = index + 1