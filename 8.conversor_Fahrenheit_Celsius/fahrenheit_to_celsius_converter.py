# 10- programa que solicite a temperatura em graus Fahrenheit ao usuário e transforme
#      a temperatura em graus Celsius. Imprima na tela. Dica: Celsius = 5 * ((Fahrenheit-32) / 9)
def conversao():
    while True:
        try:
            Fahrenheit= float(input('Digite a temperatura em graus Fahrenheit: '))
            Celsius= 5*((Fahrenheit-32)/9)
            print('A temperatura em graus Celsius é de {} °C'.format(Celsius))
            break
        except ValueError:
            print('O valor registrado necessita ser do tipo número e não pode haver vírgulas (utilize "." para separador decimal)\n')
conversao()