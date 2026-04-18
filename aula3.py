# Tipo str (string)
# Texto em Python é representado por uma sequência de caracteres, ou seja, uma string.
# As strings são delimitadas por aspas simples (' ') ou aspas duplas (" ").
# Escape de caracteres: Para incluir caracteres especiais em uma string, como aspas ou quebras de linha, usamos o caractere de escape (\).

# Exemplo de string:
nome = "João" # As aspas duplas permitem o uso de apóstrofos dentro da string sem a necessidade de escape.
sobrenome = 'Silva' # As aspas simples são úteis para strings que contêm aspas duplas, como em diálogos.
frase = "Ola, meu nome e" + " " + nome + " " + sobrenome + "!" # Concatenando strings usando o operador de adição (+).
print(frase) # Imprime a frase concatenada.

# Exemplo de escape de caracteres:
frase_com_escape = nome + " disse: \"Ola, como vai?\"" # Usando o caractere de escape para incluir aspas duplas dentro da string.
print(frase_com_escape) # Imprime a frase com as aspas duplas incluídas.
