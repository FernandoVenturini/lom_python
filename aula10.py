# PRECEDENCIA ENTRE OS OPERADORES ARITMÉTICOS

# A ordem de precedência dos operadores aritméticos é a seguinte:
# 1. Parênteses: ()
# 2. Exponenciação: **
# 3. Multiplicação, Divisão, Resto da Divisão: *, /, %
# 4. Adição e Subtração: +, -

# Exemplo 1: Sem parênteses
resultado1 = 2 + 3 * 4
print("Resultado sem parênteses:", resultado1)  # Saída: 14

# Exemplo 2: Com parênteses
resultado2 = (2 + 3) * 4
print("Resultado com parênteses:", resultado2)  # Saída: 20

# Exemplo 3: Exponenciação
resultado3 = 2 ** 3 * 4
print("Resultado com exponenciação:", resultado3)  # Saída: 32

# Exemplo 4: Resto da divisão
resultado4 = 10 % 3 + 5
print("Resultado com resto da divisão:", resultado4)  # Saída: 7

# Exemplo 5: Combinação de operadores
resultado5 = 2 + 3 * 4 - 5 ** 2
print("Resultado com combinação de operadores:", resultado5)  # Saída: -9

conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print("Resultado da conta_1:", conta_1)  # Saída: 1024