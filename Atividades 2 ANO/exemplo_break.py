numero=0
while numero <10:
    numero +=1
    if numero==5:
        print("Pulei o numero 5")
    continue
    if numero==8:
        print("Encontrei o numero 8, parando o loop")
        break
    print("numero:",numero)
print("fim do programa")