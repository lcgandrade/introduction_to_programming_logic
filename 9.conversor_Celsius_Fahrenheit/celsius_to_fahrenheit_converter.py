# 11- programa que solicite ao usuário a temperatura em graus Celsius e a transforme em Fahrenheit. 
#      Mostre o resultado na tela
def conversao():
    while True:
        try:
            Celsius= float(input('Digite a temperatura em graus Celsius: '))
            Fahrenheit= ((Celsius*9)/5)+32
            print('A temperatura em graus Fahrenheit é de {} °F'.format(Fahrenheit))
            break
        except ValueError:
            print('O valor registrado necessita ser do tipo número e não pode haver vírgulas (utilize "." para separador decimal)\n')
conversao()