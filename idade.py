
nome = input("Qual seu nome?")
idade = int(input("Qual sua idade:"))

if 1< idade <10:
    print("Parabéns, você consegue entrar como criança.")
elif 11< idade <19:
    print("Ok, você ja consegue entrar como adolecente.")
elif 20< idade <59:
    print("Ok, você está classificado como adulto.")
else:
    print("Parabéns, você entra como idoso.")