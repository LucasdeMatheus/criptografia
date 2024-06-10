# ------------------------------------- ALGORITMO DE CESAR ------------------------------------- 
def criptografar(mensagem, chave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    mensagemCriptografada = ""

    for i in mensagem:
        if ord(i) - 97 > 25 - chave:
            mensagemCriptografada += (alfabeto[ord(i) - 97 + chave - 26])
        else:
            mensagemCriptografada += (alfabeto[ord(i) - 97 + chave])
    print(mensagemCriptografada)


def descriptografar(mensagem, chave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    mensagemDescriptografada = ""

    for i in mensagem:
        if ord(i) - 97 > 25 - chave:
            mensagemDescriptografada += (alfabeto[ord(i) - 97 - chave - 26])
        else:
            mensagemDescriptografada += (alfabeto[ord(i) - 97 - chave])
    print(mensagemDescriptografada)

print()
print("Mensagem criptografada: ")
criptografar("hello", 3)

print("Mensagem descriptografada: ")
descriptografar("khoor", 3)
print()