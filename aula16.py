# if, elif, else: entendendo o fluxo do interpretador em consdicionais

# if: se
# elif: se não, se
# else: se não

# Exemplo 1: Verificar se um número é positivo, negativo ou zero
numero = float(input("Digite um numero:"))
if numero > 0:
    print("O numero e positivo.")
elif numero < 0:
    print("O numero e negativo.")
else:
    print("O numero e zero.")