def calculadora():
    print("\nCalculadora")
    n1 = float(input("\nDigite um número: "))
    op = input("Digite (+) para soma, (-) para subtração, (/) para divisão e (x) para multiplicação: ")
    n2 = float(input("Digite outro número: "))

    if op == '+':
        r = n1 + n2
        print("\nA soma entre {} e {} é igual a: {}.".format(n1, n2, r))
    elif op == '-':
        r = n1 - n2
        print("\nA subtração entre {} e {} é igual a: {}.".format(n1, n2, r))
    elif op == '/':
        r = n1 / n2
        print("\nA divisão entre {} e {} é igual a: {}.".format(n1, n2, r))
    elif op == 'x':
        r = n1 * n2
        print("\nA multiplicação entre {} e {} é igual a: {}.".format(n1, n2, r))
    else:
        print("\nOperação inválida.")

    op2 = input("\nDeseja fazer outra conta? sim(s) não(n): ")
    if op2 == 's':
        calculadora()
    else:
        exit()

calculadora()