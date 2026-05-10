# Usando funcao input para coletar dados do usuario

nome = input("Digite seu nome: ")
last_name = input("Digite seu sobrenome: ")
#print(f"O seu nome e {nome}!")
#print(f"O seu nome e {nome=}!")
#print(f"Os seu nome e {nome} {last_name}!") # concatenacao de string usando f-string"})

numero_1 = input("Digite um numero: ")
numero_2 = input("Digite outro numero: ")
print(f"A soma dos numeros e {numero_1 + numero_2}! Os numeros foram concatenados como strings!") # concatenacao de string
print(f"A soma dos numeros e {int(numero_1) + int(numero_2)}!") # convertendo string para inteiro usando a funcao int() para realizar a soma corretamente

int_numero_1 = int(numero_1) # convertendo string para inteiro usando a funcao int() e armazenando o resultado em uma nova variavel
int_numero_2 = int(numero_2) # convertendo string para inteiro usando a funcao int() e armazenando o resultado em uma nova variavel
print(f"A soma dos numeros e {int_numero_1 + int_numero_2}!") # soma correta usando variaveis do tipo inteir