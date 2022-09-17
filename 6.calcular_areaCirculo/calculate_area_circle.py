# 8- programa que solicite ao usuário o tamanho do raio de um círculo, calcule e imprima
#     na tela sua área. Dica: pi = 3.141592653589793
def circuferencia():
    raio = float(input('Digite o comprimento da circunferência de raio: '))
    c= (2*3.141592653589793) # C = 2πr
    c *= raio
    print('O comprimento da circunferência é de: {} cm'.format(c))
circuferencia()