# OPERADORES LOGICOS
# AND, OR, NOT

# AND
# O operador AND retorna True se ambos os operandos forem True, caso contrário, retorna False
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False

# OR
# O operador OR retorna True se pelo menos um dos operandos for True, caso contrário, retorna False
print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False

# NOT
# O operador NOT inverte o valor lógico do operando 
print(not True)   # False
print(not False)  # True

# EXEMPLOS DE USO
# Verificar se um número é positivo e par
numero = 4
if numero > 0 and numero % 2 == 0:
    print(f"{numero} é positivo e par.")

# Verificar se um número é negativo ou ímpar
numero = -3
if numero < 0 or numero % 2 != 0:
    print(f"{numero} é negativo ou ímpar.")

# Verificar se um número não é positivo
numero = -5
if not numero > 0:
    print(f"{numero} não é positivo.")

# Sistema:
entrada = input('[E]ntrar [S]air')
senha_digitada = input('Digite a senha:')
senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrando...')
else:
    print('Saindo...')


# AVALIACAO DE CURTO CIRCUITO
# O operador AND e OR avaliam os operandos da esquerda para a direita e param assim que o resultado seja determinado. Isso é conhecido como avaliação de curto-circuito.
# No caso do AND, se o primeiro operando for False, o resultado será False, e o segundo operando não será avaliado. No caso do OR, se o primeiro operando for True, o resultado será True, e o segundo operando não será avaliado.  
senha = input('Senha: ') or 'Sem senha'
print(f'Senha digitada: {senha}')