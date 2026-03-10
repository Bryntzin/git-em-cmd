import time
import random
import sys
 
# Animação da corrida com círculos
def CORRIDA():
    time.sleep(1.5)
    print("\nA corrida começa em:")
 
    progresso = [
        '⚫ ⚫ ⚫ ⚫',
        '🔴 ⚫ ⚫ ⚫',
        '🔴 ⚫ ⚫ ⚫',
        '🔴 🔴 ⚫ ⚫',
        '🔴 🔴 ⚫ ⚫',
        '🔴 🔴 🔴 ⚫',
        '🔴 🔴 🔴 ⚫',
        '🔴 🔴 🔴 🔴',
        '🔴 🔴 🔴 🔴',
        '⚫ ⚫ ⚫ ⚫',
       
    ]
 
    for estado in progresso:
        sys.stdout.write(f'\r{estado}')
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write('\r! V A I !   \n')
    sys.stdout.flush()
    time.sleep(1)
 
 
# Animação de carregamento genérica
def LOADING(duracao=5):
    simbolos = ['🏎️ ', '🚦', '🏁', '⚡', '🥇']
    fim = time.time() + duracao
    while time.time() < fim:
        for simbolo in simbolos:
            sys.stdout.write(f'\r{simbolo} Loading...       ')
            sys.stdout.flush()
            time.sleep(0.5)
            if time.time() >= fim:
                break
    sys.stdout.write('\rLoaded              \n')
 
 
def SISTEMACORRIDAS():
    time.sleep(1.5)
    print("Bem-vindo ao sistema: Apostas de corridas!\n")
    time.sleep(2.5)
    print("Nesta corrida temos os seguintes participantes:")
    time.sleep(0.5)
    print("---------------------------------------------->")
    time.sleep(0.5)
    print("Max Verstappen")
    time.sleep(0.5)
    print("Charles Leclerc")
    time.sleep(0.5)
    print("Daniel Bortoleto")
    time.sleep(0.5)
    print("Ayrton Senna")
    time.sleep(0.5)
    print("<----------------------------------------------\n")
    time.sleep(1.5)
 
    print("Primeiro digite a sua aposta em reais:")
    APOSTAV = float(input("R$ "))
    while APOSTAV <= 15:
        print("Aposte mais que 15 Reais.")
        APOSTAV = float(input("R$ "))
 
    print(f"Sua aposta de R${APOSTAV:.2f} foi adicionada.\n")
    time.sleep(1)
 
    print("Qual corredor você deseja apostar?")
    QCA = str(input(" "))
 
    corredores_validos = [
        "max", "max verstappen",
        "charles", "charles leclerc",
        "daniel", "daniel bortoleto",
        "ayrton", "ayrton senna"
    ]
 
    while QCA.casefold() not in corredores_validos:
        print("Entrada inválida, tente de novo:")
        QCA = str(input(" "))
 
    print("Ok, aposta feita!\n")
    time.sleep(1)
    CORRIDA()
 
 
# Início do programa
print("Abrir: / Sistema de controle de corridas? (S/N)")
ABRIR = str(input(" ")).lower()
while ABRIR not in ["s", "sim", "n", "nao", "não"]:
    ABRIR = str(input(" ")).lower()
 
if ABRIR in ["s", "sim"]:
    LOADING()
    SISTEMACORRIDAS()
else:
    print("Closed")
 
 