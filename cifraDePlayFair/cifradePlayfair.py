# ---------------------------------- ALGORITMO DE PLAYFAIR ---------------------------------- 

def excluirDuplicatas(texto):
    textoSemDuplicatas = []
    text = set()
    
    for letra in texto:
        if letra not in text:
            textoSemDuplicatas.append(letra)
            text.add(letra)
    
    return ''.join(textoSemDuplicatas).upper().replace("J", "I")


def criarAlfabeto(textoSemDuplicadas):
    alfabeto = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for letra in textoSemDuplicadas:
        alfabeto = alfabeto.replace(letra, "")

    alfabeto = textoSemDuplicadas + alfabeto
    
    matrizAlfabeto = [[],[],[],[],[]]

    index = 0
    for letra in alfabeto:
        if len(matrizAlfabeto[index]) < 5:
            matrizAlfabeto[index].append(letra)
        else:
            matrizAlfabeto[index+1].append(letra)
            index +=1

    return matrizAlfabeto
    
def dividirTexto(texto):
    texto = texto.replace(" ", "").upper().replace("Ç", "C").replace("Ã","A")
    textoDividido = []
    
    index = 0
    while index < len(texto)-1:
        duasletras = ""
        if texto[index] == texto[index+1]:
            duasletras = texto[index] + "X"
            index += 1
        else:
            duasletras = texto[index] + texto[index+1]
            index += 2
        textoDividido.append(duasletras)
    if index == len(texto) - 1:  # Se for o último caractere
            textoDividido.append(texto[index] + "X")
            index += 1

    return textoDividido

def cifrarTexto(textoDividido, alfabeto):
    def encontrarPosicao(letra, matriz):
        for linha in range(len(matriz)):
            for coluna in range(len(matriz[linha])):
                if matriz[linha][coluna] == letra:
                    return (linha, coluna)
            

    textoCifrado = []
    
    for par in textoDividido:
        letra1, letra2 = par[0], par[1]
        linha1, coluna1 = encontrarPosicao(letra1, alfabeto)
        linha2, coluna2 = encontrarPosicao(letra2, alfabeto)
        
        if linha1 == linha2:
            textoCifrado.append(alfabeto[linha1][(coluna1 + 1) % 5])
            textoCifrado.append(alfabeto[linha2][(coluna2 + 1) % 5])
        elif coluna1 == coluna2:
            textoCifrado.append(alfabeto[(linha1 + 1) % 5][coluna1])
            textoCifrado.append(alfabeto[(linha2 + 1) % 5][coluna2])
        else:
            textoCifrado.append(alfabeto[linha1][coluna2])
            textoCifrado.append(alfabeto[linha2][coluna1])
    
    return ''.join(textoCifrado)

def decifrarTexto(textoDividido, alfabeto):
    def encontrarPosicao(letra, matriz):
        for linha in range(len(matriz)):
            for coluna in range(len(matriz[linha])):
                if matriz[linha][coluna] == letra:
                    return (linha, coluna)

    textoDecifrado = []    
    for par in textoDividido:
        letra1, letra2 = par[0], par[1]
        linha1, coluna1 = encontrarPosicao(letra1, alfabeto)
        linha2, coluna2 = encontrarPosicao(letra2, alfabeto)
        
        if linha1 == linha2:
            textoDecifrado.append(alfabeto[linha1][(coluna1 - 1) % 5])
            textoDecifrado.append(alfabeto[linha2][(coluna2 - 1) % 5])
        elif coluna1 == coluna2:
            textoDecifrado.append(alfabeto[(linha1 - 1) % 5][coluna1])
            textoDecifrado.append(alfabeto[(linha2 - 1) % 5][coluna2])
        else:
            textoDecifrado.append(alfabeto[linha1][coluna2])
            textoDecifrado.append(alfabeto[linha2][coluna1])

    return "".join(textoDecifrado)

print()
chaveSemDuplicadas = excluirDuplicatas("informatica")

matrizAlfabeto = criarAlfabeto(chaveSemDuplicadas)

textoDividido = dividirTexto("Helloworld")

textoCifrado = cifrarTexto(textoDividido, matrizAlfabeto)
print("Texto criptografado:")
print(textoCifrado)

textoDecifrado = decifrarTexto(dividirTexto(textoCifrado), matrizAlfabeto)
print("Texto descriptografado:")
print(textoDecifrado)
print()