a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Voce digitou errado. \nPrimeiro bimestre: '))
b = int(input('Segundo bimestre: '))
if b > 10:
    b = int(input('Voce digitou errado. \nSegundo bimestre: '))
c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Voce digitou errado. \nTerceiro bimestre: '))
d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Voce digitou errado. \nQuarto bimestre: '))
media = (a + b + c + d) / 4
if media < 6:
    print('Aluno reprovado')
else:
    print('Aluno Aprovado')
print('Média: {}'.format(media))
