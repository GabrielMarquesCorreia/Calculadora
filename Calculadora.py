print("Calculadora")
n1 = float(input("Digite um numero : "))
op = input("Digite (+) para soma , (-) para subtracao , (%) para divisao e (x) para multiplicacao : ")
n2 = float(input("Digite outro numero : "))
if op == '+':
    r = n1 + n2
    print("A soma entre {} e {} e igual a : {}.".format(n1 , n2 , r))
elif op == '-':
    r = n1 - n2
    print("A subtracao entre {} e {} e igual a : {}".format(n1 , n2 , r))
elif op == '%':
    r = n1 / n2
    print("A divisao entre {} e {} e igual a : {}".format(n1 , n2 , r))
elif op == 'x':
    r = n1 * n2
    print("A multiplicacao entre {} e {} e igual a : {}".format(n1 , n2 , r))
    