# 3 formas diferentes de atingir o mesmo objetivo:

# 1º opção
def programa_1():
    numero1 = 1.9
    numero2 = 5.5
    # Somando dois números
    soma = numero1 + numero2
    # Mostra a soma
    print('A soma de {0} e {1} é {2}'.format(numero1, numero2, soma))
programa_1()

# 2º opção
def programa_2():
    numero3 = input('Digite o primeiro número: ')
    numero4 = input('Digite o segundo número: ')
    # Somando dois números
    soma2 = int(numero3) + int(numero4)
    # Mostra a soma
    print('A soma de {0} e {1} é {2}'.format(numero3, numero4, soma2))
programa_2()

# 3º opção
def programa_3():
    soma= 0
    qtd = 1
    while(qtd <=3):
        entrada = int(input('Digite o {}º número inteiro: '. format(qtd)))
        soma += entrada
        qtd += 1
    print('A soma dos três números inteiros é: ', soma)
programa_3()