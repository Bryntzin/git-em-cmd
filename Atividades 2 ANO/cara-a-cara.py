import time
import sys
dados= ['⚽','⚾','🏀','🏐','🏈']
def LOADING(duracao=5):
    fim = time.time() + duracao
    while time.time() < fim:
        for simbolo in dados:
            sys.stdout.write(f'\r{simbolo} Carregando...')
            sys.stdout.flush()
            time.sleep(0.5)
            if time.time() >= fim:
                break
    sys.stdout.write('\rCarregado!       \n')
print("❓bem vindo ao cara á cara,onde você terá que acertar a palavra com dicas❔")
time.sleep(1.5)
print("❕a categoria é ESPORTE❗")
time.sleep(1.5)
começo=str(input("vamos para a 1 pergunta das 5? S/N"       ))

if começo.casefold()=="s":
    time.sleep(1)
    print("A primeira dica  é: 1- é um esporte de rede")
    time.sleep(1)
    print("ja sabe qual é?")
    time.sleep(1)
    print("Tentativa:")
    tentativa=str(input())

    if tentativa.casefold()=="volei":
        LOADING()
        print("🎉 PARABENS, VOCÊ ACERTOUU!!🥳")
    else:
        LOADING()
        print("❌Você errou!❌")
        time.sleep(1)
        print("Vamos para a 2 pergunta")
        time.sleep(1)
        print("2 - é um esporte com várias categorias")

    tentativa=str(input())

    if tentativa.casefold()=="volei":
        LOADING()
        print("🎉 PARABENS, VOCÊ ACERTOUU!!🥳")
    else:
        LOADING()
        print("❌Você errou!❌")
        time.sleep(1)
        print("Vamos para a 3 pergunta")
        time.sleep(1)
        print("3 - o objetivo do esporte é fazer pontos na área do adversário")
    tentativa=str(input())

    if tentativa.casefold()=="volei":
        LOADING()
        print("🎉 PARABENS, VOCÊ ACERTOUU!!🥳")
    else:
        LOADING()
        print("❌Você errou!❌")
        time.sleep(1)
        print("Vamos para a 4 pergunta")
        time.sleep(1)
        print("4 - o esporte proibe contato fisico entre os adversários")
    tentativa=str(input())

    if tentativa.casefold()=="volei":
        LOADING()
        print("🎉 PARABENS, VOCÊ ACERTOUU!!🥳 ")
    else:
        LOADING()
        print("❌Você errou!❌")
        time.sleep(1)
        print("Vamos para a 5 pergunta")
        time.sleep(1)
        print("5 - você precisa saltar muito para conseguir pontuar")
        time.sleep(1)
        print("qual é o esporte?")
    tentativa=str(input())

    if tentativa.casefold()=="volei":
        LOADING()
        print("🎉 PARABENS, VOCÊ ACERTOUU!!🥳")
    else:
        print("A palavra era: volei    🏐")
        print("Não foi desta vez... na próxima você consegue🦾")
else:
    print("☹️  Ok então... ☹️")

