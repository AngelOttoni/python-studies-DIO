# Construção de funções anônimas (lambda)

contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['arara', 'gato', 'girafa']
print(contador_letras(lista_animais))

# Calculadora:

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(soma(57, 144))
print(subtracao(105,54))

# OU

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}

print(type(calculadora))
soma = calculadora['soma'] # Isso é o mesmo que a linha 21
#soma = lambda a, b: a + b
multiplicacao = calculadora['multiplicacao']
print('A soma é: {}'.format(soma(10, 5)))
print('A multiplicação é: {}'.format(multiplicacao(10, 2)))