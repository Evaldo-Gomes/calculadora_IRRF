# Sistema para recolhimento de IR com base no salário
import IRRF_calc

# Por padrão o sistema calcula com a regra antiga
regraAtual = False

# Apresentação
print('\n\t\t\t -- Simulador para Recolhimento de IRPF --\n')

# Entradas
salarioBruto = float(input('Informe o salário: '))
dependentes = int(input('Informe o número de dependentes: '))

#checkbox
atual = input('Rendimento recebido a partir de maio/2023 (s/n)? ')
if atual.lower() == 's':
    regraAtual = True

# Processamento
impostoRenda = IRRF_calc.imposto(salarioBruto, dependentes, regraAtual)
print('\n\t\t\t -- Dados do IR --\n')
print('Salário Bruto..............R$ {:.2f}'.format(impostoRenda['salarioBruto']))
print('Núm. de dependentes.................{}'.format(impostoRenda['dependentes']))
print('-'*40)
print('Salário Base................R$ {:.2f}'.format(impostoRenda['salarioBase']))
print('Alíquota........................{:.2f}%'.format((impostoRenda['taxa']*100)))
print('IR Devido....................R$ {:.2f}'.format(impostoRenda['irDevido']))
print('-'*40)
print('Salário Líquido.............R$ {:.2f}'.format(impostoRenda['salarioLiquido']))
print('Alíquota Efetiva.................{:.2f}%'.format((impostoRenda['taxaEfetiva']*100)))

print(impostoRenda)