# 4- programa que solicite ao usuário um nome de fruta e então mostre a seguinte mensagem na tela:
#    “A fruta digitada foi: <nome da fruta digitada>”.
def fruta():
    nome = input('Digite um nome de fruta: ')
    if nome !="":
        print('A fruta digitada foi {}'.format(nome))
    else:
        print('A informação não foi registrada')
fruta()