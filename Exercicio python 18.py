numero = int(input("Digite um número: "))

if numero == 0:
    print("Neutro")
elif numero % 2 == 0 and numero > 0:
    print("Par positivo")
elif numero % 2 == 0 and numero < 0:
    print("Par negativo")
elif numero % 2 != 0 and numero > 0:
    print("Ímpar positivo")
else:
    print("Ímpar negativo")