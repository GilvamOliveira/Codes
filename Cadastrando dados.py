from datetime import date

# Coletando dados do usuário
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
dia = int(input('Digite o dia do seu nascimento (Ex: 10): '))
mes = int(input('Digite o mês do seu nascimento (Ex: 5): '))
ano = int(input('Digite o ano do seu nascimento (Ex: 1995): '))
altura_metros = float(input('Digite sua altura em metros (Ex: 1.70): '))

# Calculando informações
data_nascimento = date(ano, mes, dia)
hoje = date.today()
idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.today))
dias_de_vida = hoje - data_nascimento
maior_de_idade = idade >= 18

# Exibindo os dados
print('\n=== DADOS CADASTRADOS ===\n')
print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade, 'anos')
print('Data de nascimento:', data_nascimento.strftime('%d/%m/%y'))
# Maior de idade?
if  maior_de_idade:
    print('Você é maior de idade!')
else:
    print('Você é menor de idade!')

print('Tempo de vida (em dias):', dias_de_vida.days, 'dias')
print('Altura em metros:', altura_metros, 'metros')
