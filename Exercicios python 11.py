numero= int(input("Digite um número: "))
if numero % 2 == 0 and numero > 0:
    print("Par positivo")
elif numero % 2 == 0 and numero < 0:
    print("Par negativo")
else:
    print("Impar")