def calculadora():
    print("\nCalculadora")
    n1 = float(input("\nDigite um número: "))
    op = input("Digite (+) para soma, (-) para subtração, (/) para divisão e (x) para multiplicação: ")
    n2 = float(input("Digite outro número: "))

    if op == '+':
        r = n1 + n2
        print(f"\nA soma entre {n1} e {n2} é igual a: {r:.2f}.")
    elif op == '-':
        r = n1 - n2
        print(f"\nA subtração entre {n1} e {n2} é igual a: {r:.2f}.")
    elif op == '/':
        r = n1 / n2
        print(f"\nA divisão entre {n1} e {n2} é igual a: {r:.2f}.")
    elif op == 'x':
        r = n1 * n2
        print(f"\nA multiplicação entre {n1} e {n2} é igual a: {r:.2f}.")
    else:
        print("\nOperação inválida.")

    op2 = input("\nDeseja fazer outra conta? sim(s) não(n): ")
    if op2 == 's':
        calculadora()
    else:
        exit()

calculadora()