# Descrição: Menu Simples

print("## Menu ##")
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

opção = 0
while opção != 5:
    print("[1] Soma \n [2] Subtração \n [3] Multiplicação \n [4] Divisão \n [5] Sair do Programa\n ")
    opção = int(input("Qual a sua opção: "))

    if opção == 1:
        soma = n1 + n2
        print("A soma entre os valores é {}".format(soma))
    elif opção == 2:
        subtracão = n1 - n2
        print("A subtração entre os valores é {}".format(subtracão))
    elif opção == 3:
        multiplicação = n1 * n2
        print("A multiṕlicação entre os valores é {}".format(multiplicação))
    elif opção == 4:
        divisao = n1 / n2
        print("A soma entre os valores é {}".format(divisao))
    elif opção == 5:
        print("Obrigado por usar o progrma! Volte sempre!")
    print("#"*50)
else:
    print("*"*10)











