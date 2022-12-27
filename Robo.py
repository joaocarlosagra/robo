# Robo #
# Autor: João Carlos Agra dos Santos #

# Criar um programa que

print()
print("-"*40)
print()
print("Bem vindo a Bendito.")
print()
print("-"*40)
print()
a1 = 4

if a1==4:
    print("Digite a opção desejada.")
    print("1 - Comercial")
    print("2 - Financeiro")
    print("3 - Suporte")
    print("4 - Voltar")
    print("5 - Sair")
    a1 = int(input())
    if a1==1:
        print("Ola sou Tawan.")
        print("Que produto gostaria de adquirir?")
        print("1 - Produto: ")
        print("4 - Voltar")
        a2 = int(input())
    elif a1==2:
        print("Ola, sou Manuela.")
        print("O que deseja do setor financeiro?")
        print("1 - Boleto. ")
        print("4 - Voltar")
        a3 = int(input())
    elif a1==3:
        print("Ola, sou Artur.")
        print("No que posso ajudar?")
        print("1 - Atendente. ")
        print("4 - Voltar")
        a4 = int(input())
    elif a1==5:
        print("Obrigado por passar aqui.")
else :
    print("Vamos começar novamente.")
    
