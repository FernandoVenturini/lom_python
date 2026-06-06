# OPERADOR LOGICO NOT

# O operador lógico NOT é utilizado para inverter o valor lógico de uma expressão. Ele é representado pelo símbolo "not" em Python.
# Exemplo de uso do operador lógico NOT:
# Suponha que temos uma variável que indica se um aluno passou ou não em um exame
passou_exame = True
# Agora, queremos verificar se o aluno não passou no exame
if not passou_exame:
    print("O aluno nao passou no exame.")
else:
    print("O aluno passou no exame.")
# Neste exemplo, a expressão "not passou_exame" inverte o valor de "passou_exame". Como "passou_exame" é True, "not passou_exame" se torna False, e o bloco de código dentro do "else" é executado, resultando na mensagem "O aluno passou no exame." sendo impressa.

senha = input("Digite a senha: ")
if not senha == "123456":
    print("Senha incorreta.")
else:
    print("Senha correta.")
# Neste exemplo, a expressão "not senha == '123456'" verifica se a senha digitada pelo usuário é diferente de "123456". Se a senha for diferente, a mensagem "Senha incorreta." será impressa. Caso contrário, a mensagem "Senha correta." será exibida.