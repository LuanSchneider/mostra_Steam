equacao = input('Qual equação você deseja fazer?')

if equacao == 'mais':
    n1 = float(input('Qual seu primeiro numero?'))
    n2 = float(input('Qual seu segundo numero?'))
    total = n1 + n2
    print('Seu total é {}'.format(total))
else:
    print('Adeus!')
