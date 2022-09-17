# 5- programa que receba a distância de uma cidade em quilômetros e a transforme em metros, 
#     mostrando o resultado na tela.
def distancia():
    km = int(input('Digite a distância entre duas cidades em km: '))
    mts = km * 1000
    print('A distância em metros é de: {}'.format(mts))
distancia()