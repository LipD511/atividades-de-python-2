a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
print("Soma:", a + b)
if a > b:
    print("O maior é:", a)
elif b > a:
    print("O maior é:", b)
else:
    print("Os números são iguais")