# INTRODUCAO AOS BLOCOS DE CODIGO if/elif/else

# if/elif/else é uma estrutura de controle de fluxo que permite executar diferentes blocos de código com base em condições específicas

entrada = input("Voce quer entrar ou sair do sistema? (entrar/sair): ")

if entrada == 'entrar':
    print("Voce entrou no sistema!")
elif entrada == 'sair':
    print("Voce saiu do sistema!")
else: 
    print("Entrada invalida! Por favor, digite 'entrar' ou 'sair'.")