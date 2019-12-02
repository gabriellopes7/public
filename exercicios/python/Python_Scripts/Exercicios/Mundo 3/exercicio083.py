e = input('Digite uma expressão: ')
pilha =[]
for simb in e:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append('.')
if len(pilha)==0:
    print('Expressão válida !')
else:
    print('Expressão inválida !')