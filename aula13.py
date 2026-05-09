# FORMATCAO DE STRINGS COM O METODO .FORMAT()

letra1 = 'A'
letra2 = 'B'
letra3 = 'C'
numero1 = 1.1

string = 'letra1={} letra2={} letra3={} numero1={:.2f}'
formato = string.format(letra1, letra2, letra3, numero1)

print(formato)
