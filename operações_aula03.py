a = int(input('entre com o primeiro valor: '))
b = int(input('entre com o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultado = ('Soma: {soma}. \nSubtracao: {subtracao}. '
             '\nMultiplicacao: {multiplicacao}. '
             '\nDivisao: {divisao}. '
             '\nResto: {resto}'.format(soma=soma,
                                       subtracao=subtracao,
                                       multiplicacao=multiplicacao,
                                       divisao=divisao,
                                       resto=resto))
print(resultado)
