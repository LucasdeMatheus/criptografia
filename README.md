<h1 align="center"> Criptografia </h1>

# Índice 

* [Índice](#índice)
* [Descrição](#descrição)
* [Algoritmos](#algoritmos)
* [Tecnologias utilizadas](#tecnologias-utilizadas)



# Descrição
<p>Este repositório contém implementações de vários algoritmos de criptografia. Cada algoritmo é documentado com uma descrição detalhada, passos do algoritmo, exemplos de funcionamento, análise de complexidade e implementação em Python.</p>

# Algoritmos

  * [Cifra de Cesar](#cifra-de-cesar)
  * [Cifra de Vigenere](#cifra-de-vigenere)
  * [Cifra de Rail Fence](#cifra-de-rail-fence)
  * [Cifra de Play Fair](#cifra-de-play-fair)
## Cifra de Cesar
### Descrição
<p>A Cifra de Cesar é uma técnica de criptografia simples onde cada letra do texto é deslocada um número fixo de posições no alfabeto.
</p>

### Lógica
1. Escolha um número de deslocamento (chave).
2. Para cada letra do texto, desloque-a no alfabeto pelo número de posições definido pela chave.
3. Se o deslocamento passar do final do alfabeto, continue do início.

### Demonstração
<p>
mensagem: hello
<br>chave: 3
<br>criptografia: khoor</p>

<br>

### output:
<p>
<img loading="lazy" src="https://github.com/LucasdeMatheus/criptografia/assets/134244848/5fe26bdf-5896-458e-b0a7-69b323022c00"width=500/>
<br>
 
</p>
<br>

## Cifra de Vigenere

### Descrição
<p>A Cifra de Vigenère é uma técnica de criptografia que utiliza uma palavra-chave para determinar o deslocamento de cada letra do texto, tornando a cifra mais complexa e segura do que a Cifra de César.</p>

### Lógica

1. Escolha de uma palavra-chave (chave):
<Br>1.1 A palavra-chave é repetida ou truncada para igualar o comprimento do texto a ser criptografado.
2. Preparação da chave:
<br>2.1 Cada letra da chave corresponde a um deslocamento baseado em sua posição no alfabeto (A = 0, B = 1, ..., Z = 25).
3. Criptografia:
<br>3.1 Para cada letra do texto, determine o deslocamento usando a letra correspondente da chave.
<br>3.2 Desloque a letra do texto pelo número de posições indicado pela letra da chave.
<br>3.3 Se o deslocamento passar do final do alfabeto, continue do início.
4. Descriptografia:
<br>4.1 Utilize a mesma chave para determinar o deslocamento, mas em sentido contrário para cada letra do texto cifrado.
<br>4.2 Desloque cada letra do texto cifrado para trás pelo número de posições indicado pela letra da chave.

### Demonstração

<p>
mensagem: hello
<br>chave: world
<br>criptografia: DSCWR </p>
 <br>
 
### output:

 <p>
<img loading="lazy" src="https://github.com/LucasdeMatheus/criptografia/assets/134244848/c4faaaf1-dcc1-4e05-8066-e67f4d4c964f"width=500/>
<br>
 </p>

## Cifra de Rail Fence

### Descrição:
A Cifra de Rail Fence é uma técnica de transposição simples utilizada na criptografia. Nesta técnica, as letras da mensagem original são escritas em um padrão de zigue-zague em várias "cercas" ou linhas, daí o nome "Rail Fence". 

### Lógica

Definição da Chave:

A chave é o número de linhas (cercas) a serem utilizadas na cifra.

Criptografia:

1. Escreva a mensagem original em um padrão de zigue-zague nas linhas da matriz.
2. Comece a preencher a matriz linha por linha até atingir a última linha, então mude a direção para cima até voltar à primeira linha e repita o processo.
3. Leia as letras linha por linha para formar a mensagem cifrada.

### Demonstração

<p>
mensagem: HELLOWORLD
<br>chave: 3
<br>criptografia: HOLELWRDLO </p>
 <br>

### output:
<p>
<img loading="lazy" src="https://github.com/LucasdeMatheus/criptografia/assets/134244848/64382468-a9bd-4946-9e18-b6b1211ea224"width=500/>

## Cifra de Play Fair

Descrição:
A cifra de Playfair é um método de criptografia de substituição poligráfica que opera em pares de letras. Ela foi desenvolvida por Charles Wheatstone em 1854, mas foi popularizada por Lyon Playfair. Ao contrário das cifras de substituição simples, a cifra de Playfair substitui pares de letras, aumentando a segurança da criptografia.

Lógica da Cifra de Playfair:

Definição da Chave:

Escolha uma palavra ou frase como chave. Remova letras duplicadas e substitua 'J' por 'I' para caber na matriz 5x5.

Criação da Matriz 5x5:

Preencha a matriz 5x5 com a chave, seguida pelas letras restantes do alfabeto que não estão na chave.

Preparação do Texto:

Remova espaços e converta todas as letras para maiúsculas. Divida o texto em pares de letras, inserindo 'X' entre letras duplicadas e no final, se necessário.

### Criptografia:

1. Para cada par de letras, use as regras de substituição da cifra de Playfair:
2. Se as letras estão na mesma linha, substitua cada letra pela letra imediatamente à direita.
3. Se as letras estão na mesma coluna, substitua cada letra pela letra imediatamente abaixo.
4. Se as letras formam um retângulo, substitua cada letra pela letra na mesma linha da outra letra do par.

### Demonstração

mensagem: hello World
chave: informatica
criptografia: KGQVSIYNIUGV

### output:

<p>
<img loading="lazy" src="https://github.com/LucasdeMatheus/criptografia/assets/134244848/21cd17d0-81f4-4a4e-bbaf-beeb72367848"width=500/>

Obs: nesta criptografia, optei não adicionar funcionalidade para remover a letra X para evitar bugs com palavras que possuem X.

# Tecnologias Utilizadas

 <p>linguagem: Python
<br>IDE: Visual Studio Code</p>
