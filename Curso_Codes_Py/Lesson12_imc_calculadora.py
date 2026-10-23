# Calculadora de IMC com classificação

# Solicita os dados do usuário
nome = input('Digite seu nome: ')
altura_metros = float(input('Digite sua altura em metros (Ex: 1.70): '))
peso = float(input('Digite seu peso em kilogramas (Ex: 62.55): '))

# Calcula o IMC
imc = peso / (altura_metros ** 2)

# Define a classificação do IMC
if imc < 18.5:
    classificacao = 'Abaixo do peso'
elif imc < 25:
    classificacao = 'Peso normal'
elif imc < 30:
    classificacao = 'Sobrepeso'
elif imc < 35:
    classificacao = 'Obesidade grau I'
elif imc < 40:
    classificacao = 'Obesidade grau II (severa)'
else:
    classificacao = 'Obesidade grau III (mórbida)'

# Exibe o resultado
print(f'{nome} tem {altura_metros:.2f}m de altura, pesa {peso:.2f}kg e seu IMC é {imc:.2f}')
print(f'Classificação: {classificacao}')
