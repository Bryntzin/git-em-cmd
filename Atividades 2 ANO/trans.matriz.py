def processa_comando(comando):
    match comando:
        case "iniciar":
            print("Comando de iniciar executado")
        case "pausar":
            print("Comando de pausar executado")
        case "parar":
            print("Comando de parar executado")
        case _: # Corresponde a qualquer outro caso (o 'default')
            print("Comando desconhecido")

processa_comando("iniciar")
# Saída: Comando de iniciar executado

processa_comando("reiniciar")
# Saída: Comando desconhecido