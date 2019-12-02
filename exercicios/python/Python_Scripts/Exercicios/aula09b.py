frase = ' Curso em Vídeo Python '
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[12:])
print(frase[1:15:2])
print("""Welcome! Are you completely new to programing ?
about why and how to get started with python. Fortunately
and experienced programmer bla bla bla
Its also easy for beginners""")
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.strip().replace('Python','Android'))
print('Curso' in frase)
print(frase.strip().find('Curso'))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])