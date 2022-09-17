# 9- programa que pergunte ao usuário o valor que ele tem investido e a taxa percentual
#     que ele ganha ao mês (juros simples). Calcule e imprima o total ganho com o investimento em 3 meses.
def investimento():
    while True:
        try:
            C= float(input('Digite o capital inicial: '))
            i= float(input('Digite a taxa de juros: '))
            t= int(input('Digite o período da operação: '))
            J= C*(i/100)*t 
            C+=J
            print('O valor dos juros é de: {}'.format(J))
            print('O montante final é de: {}'.format(C))
            break
        except ValueError:
            print('O valor registrado necessita ser do tipo número e não pode haver vírgulas (utilize "." para separador decimal)\n')
investimento()