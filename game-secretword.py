palavra = input('Digite uma palavra para começar o Jogo: '.upper())
secreta = palavra
digitadas = []
chances = 3

while True:
    letra = input('Digite uma letra: ')
    if len(letra) > 1 and letra == '':
        print('OPS, você só pode digitar uma letra')
        continue

    digitadas.append(letra)

    if letra in secreta:
        print(f'UHHHULL, essa letra existe na palavra.')
    else:
        print(f'OPS, essa letra NÃO existe em na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreta:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreta:
        print(f'QUE LEGALLLL! Você acertou a palavra secreta é "{secreto_temporario}"')
        break
    else:
        print(f'a palavra secreta está assim {secreto_temporario}')
