import random
import funcoes

jogo = 'forca'

def jogar():
    enforcou = False
    acertou = False
    erros = 0

    funcoes.bem_vindo(jogo)                     # Mensagem de boas vindas
    palavra_secreta = funcoes.ler_txt()     # Faz a leitura das palavras de um arquivo
    letras_acertadas = funcoes.inicializa_letras_acertadas('_', palavra_secreta) # Repetindo string com quantidade caracteres
    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = funcoes.solicita_chute() # Solicita o chute ao usuário

        # '.upper' para letra maiúscula
        # '.lower' para letra minúscula
        if(chute in palavra_secreta):
            funcoes.marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros = erros + 1
            print(f'Você errou, {erros} de 7.')
            funcoes.desenha_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

        if ("_" not in letras_acertadas):
            funcoes.mensagem_ganhador(pontos=0)
        elif (erros == 6):
            funcoes.mensagem_perdedor(palavra_secreta)
    funcoes.fim_jogo()

if(__name__ == "__main__"):
    jogar()
