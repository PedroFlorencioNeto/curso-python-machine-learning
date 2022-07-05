# ------------------------------------------------------------------------------------ #

# Oficina 1.1 - Paradigma da Programação Funcional em Python

# Por: Pedro Florencio de Almeida Neto - pedroflorencio@alu.ufc.br

# ------------------------------------------------------------------------------------ #

# 1. Quantas músicas ruins, medianas e boas existem para cada gênero (Rock e Pop)?

notas_rock = [5, 1, 4, 0, 2, 5, 2, 1, 0, 5, 5, 3, 5, 2, 5, 5, 3, 5, 4, 4]
notas_pop = [3, 2, 5, 1, 2, 1, 4, 1, 5, 0, 4, 2, 1, 2, 5, 2, 4, 4, 0, 1]

# Função de categoriza as notas das músicas

# Ruins: 0 a 1
# Medianas: 2 a 3
# Boas: 4 a 5

def categoria(nota):
    if nota < 2:
        return 'ruim'
    elif nota > 1 and nota < 4:
        return 'mediana'
    else:
        return 'boa'

# Aplicação da função de categorização na lista de notas de cada gênero
classificacao_rock = list(map(categoria,notas_rock))
classificacao_pop = list(map(categoria,notas_pop))

# Quantidade de notas ruins para cada gênero
qtde_ruins_rock = len(list(filter(lambda x:x=='ruim',classificacao_rock)))
qtde_ruins_pop = len(list(filter(lambda x:x=='ruim',classificacao_pop)))

# Quantidade de notas medianas para cada gênero
qtde_medianas_rock = len(list(filter(lambda x:x=='mediana',classificacao_rock)))
qtde_medianas_pop = len(list(filter(lambda x:x=='mediana',classificacao_pop)))

# Quantidade de notas boas para cada gênero
qtde_boas_rock = len(list(filter(lambda x:x=='boa',classificacao_rock)))
qtde_boas_pop = len(list(filter(lambda x:x=='boa',classificacao_pop)))

print('\nQuestão 1\nRock: {} ruins, {} medianas e {} boas. Pop: {} ruins, {} medianas e {} boas.'.format(
    qtde_ruins_rock, qtde_medianas_rock, qtde_boas_rock,
    qtde_ruins_pop, qtde_medianas_pop, qtde_boas_pop
))

# ------------------------------------------------------------------------------------ #

# 2. Existe alguma música mediana de Rock?

print('\nQuestão 2\nExiste música mediana de Rock? {}'.format(any(list(filter(lambda x:x=='mediana',classificacao_rock)))))

# ------------------------------------------------------------------------------------ #

# 3. Qual gênero musical teve uma maior quantidade de músicas boas?

if qtde_boas_pop > qtde_boas_rock: print('\nQuestão 3\n Tem mais músicas boas de Rock\n')
else: print('\nQuestão 3\n Tem mais músicas boas de Rock\n')

# ------------------------------------------------------------------------------------ #