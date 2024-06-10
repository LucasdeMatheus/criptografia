def criptografar(mensagem, chave):
    matriz = [['' for _ in range(len(mensagem))] for _ in range(chave)]

    linha = 0
    direcao = 1 

    for coluna in range(len(mensagem)):
        matriz[linha][coluna] = mensagem[coluna]
        if linha == 0:
            direcao = 1
        elif linha == chave - 1:
            direcao = -1
        linha += direcao

    mensagemCifrada = []
    for linha in matriz:
        for i in range(len(mensagem)):
            if linha[i] != "":
                mensagemCifrada.append(linha[i])
    return ''.join(mensagemCifrada)



def descriptografar(mensagemCifrada, chave):
    matriz = [['' for _ in range(len(mensagemCifrada))] for _ in range(chave)]

    linha = 0
    direcao = 1 
    for coluna in range(len(mensagemCifrada)):
        matriz[linha][coluna] = ' '
        if linha == 0:
            direcao = 1
        elif linha == chave - 1:
            direcao = -1
        linha += direcao

    index = 0
    for i in range(chave):
        for j in range(len(mensagemCifrada)):
            if matriz[i][j] == ' ' and index < len(mensagemCifrada):
                matriz[i][j] = mensagemCifrada[index]
                index += 1

    mensagemDecifrada = []
    linha = 0
    direcao = 1
    for i in range(len(mensagemCifrada)):
        mensagemDecifrada.append(matriz[linha][i])
        if linha == 0:
            direcao = 1
        elif linha == chave - 1:
            direcao = -1
        linha += direcao

    return ''.join(mensagemDecifrada)

mensagem = "HELLOWORLD"
chave = 3
mensagemCifrada = criptografar(mensagem, chave)
print()
print("Mensagem Cifrada:\n", mensagemCifrada)
mensagemDecifrada = descriptografar(mensagemCifrada, chave)
print("Mensagem Decifrada:\n", mensagemDecifrada)
print()
