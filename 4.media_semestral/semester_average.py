# 6- programa que solicite ao usuário duas notas semestrais e retorne na tela a média final da disciplina.
def notas():
    soma = 0
    qtd = 1
    while qtd <= 2:
        nota = float(input('Digite a {}º nota do aluno no semestre: '.format(qtd)))
        soma += nota
        qtd += 1
    print('A média do aluno no semestre é de: {}'.format(soma / 2))
notas()