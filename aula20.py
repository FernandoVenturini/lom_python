# EXERCICIO OPERADOR DE COMPARACAO

primeiro_valor = int(input("Digite um numero: "))
segundo_valor = int(input("Digite outro numero: "))

if primeiro_valor > segundo_valor:
    print(
        f'O primeiro valor e {primeiro_valor=} e maior '
        f'do que {segundo_valor=} '
    )
elif primeiro_valor < segundo_valor:
    print("O primeiro valor é menor que o segundo valor.")
else:
    print("Os dois valores são iguais.")