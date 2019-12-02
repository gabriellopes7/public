palavras = ('Arara','Padeiro','Rock Content','Brasil','Gabriel','Oliveira')
for p in palavras:
    print(f'Em {p} temos ',end='')
    for letra in p.lower():
        if letra in 'aeiou': #busca se há a letra no conteúdo de vogais
            print(letra,end=' ')
    print('')