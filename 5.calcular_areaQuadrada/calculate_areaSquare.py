# 7- programa que receba o tamanho de um lado de um quadrado e calcule sua área,
#     mostrando na tela a área desse quadrado.
def area():
    entrada = float(input('Digite o tamanho de um lado de um quadrado: '))
    entrada *= entrada
    print('A área do quadrado é de: {} cm2'.format(entrada))
area()